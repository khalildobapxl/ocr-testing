import pytesseract
from PIL import Image
from _images import all_images

def ocr_with_tesseract(image_path):
    """
    Perform OCR on the given image using Tesseract OCR.

    """
    try:
        # Open the image file
        img = Image.open(image_path)
        
        # Use Tesseract to do OCR on the image
        extracted_text = pytesseract.image_to_string(img)

        print(f"--- Tesseract Output for {image_path} ---")
        print(extracted_text)
        print("------------------------")

    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        

if __name__ == "__main__":
    for image_path in all_images:
        ocr_with_tesseract(image_path)

    # Specific test case for textImage.png
    textImage = "../testImages/textImage.png"
    ocr_with_tesseract(textImage)


