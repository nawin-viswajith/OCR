import pytesseract
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import cv2

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

        self.text_box = tk.Text(root, height=10, width=50)
        self.text_box.pack()

        self.perform_ocr_button = tk.Button(root, text="Perform OCR", command=self.perform_ocr)
        self.perform_ocr_button.pack()

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image(self.image)

    def capture_image(self):
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.image = Image.fromarray(frame)
            self.display_image(self.image)
        camera.release()

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

if __name__ == "__main__":
    root = tk.Tk()
    app = OCRApplication(root)
    root.mainloop()
