from paddleocr import PaddleOCR
import os
from image_loader import get_images_from_folder  # Using the no-dialog version

print("Loading PaddleOCR model...")

# --- THIS IS THE FIXED LINE ---
# We removed all max_side arguments to stop the crash.
# We will get a warning about resizing, but it won't stop the script.
ocr = PaddleOCR(use_textline_orientation=True, lang="en")

print("PaddleOCR Model loaded.")

def ocr_with_paddle(image_path):
    """
    Perform OCR on the given image using PaddleOCR.
    """
    filename = os.path.basename(image_path)
    try:
        result = ocr.ocr(image_path) 
        
        print(f"--- PaddleOCR Output for {filename} ---")
        
        if result and result[0]:
            for item in result[0]:
                # This safety check is the most important part
                if item[1] and len(item[1]) == 2:
                    text = item[1][0]
                    confidence = item[1][1]
                    print(f"  Detected text: {text} (Confidence: {confidence:.4f})")
                else:
                    print(f"  [Found a box, but recognition failed for this item]")
        else:
            print("  No text detected.")
            
        print("-" * (len(filename) + 26) + "\n")

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred while processing {filename}:")
        print(f"  ERROR: {e}\n")

if __name__ == "__main__":
    
    images_to_test = get_images_from_folder()
    
    if images_to_test:
        print("\nStarting PaddleOCR process...\n")
        for image_path in images_to_test:
            ocr_with_paddle(image_path)
        print("--- All tests complete! ---")
    else:
        print("No images were found or selected.")