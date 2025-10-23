import easyocr
import os  
from image_loader import get_images_from_folder 

reader = easyocr.Reader(['en'])  # Initialize the EasyOCR reader

def ocr_with_easyocr(image_path):
    """
    Perform OCR on the given image using EasyOCR.
    """
    filename = os.path.basename(image_path)  
    try:
        result = reader.readtext(image_path)
        
        print(f"--- EasyOCR Output for {filename} ---")
        for (bbox, text, prob) in result:
            print(f"  Detected text: {text} (Confidence: {prob:.2f})")
        print("-" * (len(filename) + 24) + "\n") 

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred while processing {filename}: {e}\n")


if __name__ == "__main__":
    
    # Call the function to let the user choose a folder
    images_to_test = get_images_from_folder()
    
    # Run the tests on the list of images it returned
    if images_to_test:
        print("\nStarting EasyOCR process...\n")
        for image_path in images_to_test:
            ocr_with_easyocr(image_path)
        print("--- All tests complete! ---")
    else:
        print("No images were found or selected.")