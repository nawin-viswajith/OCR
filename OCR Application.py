import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance
import cv2
import numpy as np
import pytesseract

class OCRApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Handwritten Text Recognition")

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.select_image_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_image_button.pack()

        self.capture_image_button = tk.Button(root, text="Capture From Camera", command=self.capture_image)
        self.capture_image_button.pack()

        self.text_label = tk.Label(root, text="Recognized Text:")
        self.text_label.pack()

        self.text_box = tk.Text(root, height=10, width=70)
        self.text_box.pack()

        self.perform_ocr_button = tk.Button(root, text="Perform OCR", command=self.perform_ocr)
        self.perform_ocr_button.pack()

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image(self.preprocess_image(self.image))

    def capture_image(self):
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.image = Image.fromarray(frame)
            self.display_image(self.preprocess_image(self.image))
        camera.release()

    def preprocess_image(self, image):
        enhancer = ImageEnhance.Sharpness(image)
        sharpened_image = enhancer.enhance(2.0)
        
        opencv_image = np.array(sharpened_image)
        
        aligned_image = self.align_text(opencv_image)
        aligned_pil_image = Image.fromarray(aligned_image)
        
        return aligned_pil_image  

    def align_text(self, image):
        img_thresh = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        _, img_thresh = cv2.threshold(img_thresh, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        coords = np.column_stack(np.where(img_thresh > 0))
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        h, w = image.shape[:2]  # Ensure shape is properly extracted for both OpenCV 3 and 4

        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(img_thresh, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    
        return rotated

    def display_image(self, image):
        image.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def perform_ocr(self):
        if hasattr(self, 'image'):
            text = pytesseract.image_to_string(self.image)
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.END, text)
        else:
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.END, "Please select an image or capture from camera first.")

root = tk.Tk()
app = OCRApplication(root)
root.mainloop()
