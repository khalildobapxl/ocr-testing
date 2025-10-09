from paddleocr import PaddleOCR
from _images import all_images

print("Loading PaddleOCR model...")
ocr = PaddleOCR(use_angle_cls=True, lang="en")
print("Model loaded.")

def ocr_with_paddle(image_path):
    """
    Perform OCR on the given image using PaddleOCR.

    """
    try:
        # Use PaddleOCR to do OCR on the image
        result = ocr.ocr(image_path)

        print(f"--- PaddleOCR Output for {image_path} ---")
        for line in result:
            line.print() 
        print("------------------------")

    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    for image_path in all_images:
        ocr_with_paddle(image_path)
    