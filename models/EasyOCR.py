import easyocr
from _images import all_images
reader = easyocr.Reader(['en'])  # Initialize the EasyOCR reader with English language support

def ocr_with_easyocr(image_path):
    """
    Perform OCR on the given image using EasyOCR.

    """
    try:
        # Use EasyOCR to do OCR on the image
        result = reader.readtext(image_path)

        print(f"--- EasyOCR Output for {image_path} ---")
        for (bbox, text, prob) in result:
            print(f"Detected text: {text} (Confidence: {prob:.2f})")
        print("------------------------")

    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    for image_path in all_images:
        ocr_with_easyocr(image_path)
