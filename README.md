# Handwritten Text Recognition

This is a simple Python application for performing Handwritten Text Recognition (HTR) using the Tesseract OCR engine. It allows users to either select an image file or capture an image from the camera for recognition.

## Features

- Select an image file (JPEG, JPG, PNG) from your local filesystem.
- Capture an image from your camera directly within the application.
- Perform OCR on the selected/captured image to recognize handwritten text.
- Display the recognized text in a text box within the application.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- Pillow (`PIL`)
- Tesseract OCR (`pytesseract`)
- Tkinter

## Installation

1. Clone the repository or download the source code as a ZIP file.
2. Install the required Python packages using pip:

```bash
pip install opencv-python pillow pytesseract
```

## Usage
1. Run the ocr_application.py file.
2. Click on the "Select Image" button to choose an image file from your local filesystem.
3. Alternatively, click on the "Capture From Camera" button to capture an image using your camera.
4. Click on the "Perform OCR" button to initiate the OCR process.
5. The recognized text will be displayed in the text box below the image.

## Expected Updates
1. Manual region selection.
2. Enhanced accuracy.
3. Better image preview.
