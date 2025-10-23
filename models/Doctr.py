from doctr.io import DocumentFile
from doctr.models import ocr_predictor
import os
from image_loader import get_images_from_folder  # <-- IMPORT YOUR FUNCTION

# --- 1. Initialize the OCR Predictor ---
print("Loading DocTR model...")
# CORRECT for newer versions
model = ocr_predictor(
    det_arch='db_resnet50',        # Text detection backbone
    detect_language=True,       # Recognition model that supports multilingual scripts
    pretrained=True             # Use pretrained multilingual weights
)

print("Model loaded.")


def ocr_with_doctr(image_path):
    """
    Performs OCR on an image file using DocTR and prints the results.
    """
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' was not found.")
        return

    
    # --- 2. Load the image as a Document ---
    # Using os.path.basename to get just the filename for cleaner output
    filename = os.path.basename(image_path)
    print(f"Analyzing {filename}...")
    
    try:
        doc = DocumentFile.from_images(image_path)
        
        # --- 3. Run the prediction ---
        result = model(doc)

        # --- 4. Process and Display Results ---
        print(f"\n--- DocTR Output for {filename} ---")
        for page in result.pages:
            for block in page.blocks:
                for line in block.lines:
                    # Reconstruct the line from individual words
                    line_text = ' '.join([word.value for word in line.words])
                    confidence = min([word.confidence for word in line.words]) if line.words else 0
                    print(f"  Text: {line_text} | Min Confidence: {confidence:.4f}")

    except Exception as e:
        print(f"An error occurred while processing {filename}: {e}")
    
    print("-" * (len(filename) + 21) + "\n")


# --- THIS IS THE MODIFIED SECTION ---
if __name__ == "__main__":
    
    # 1. Call the function to let the user choose a folder
    images_to_test = get_images_from_folder()
    
    # 2. Run the tests on the list of images it returned
    if images_to_test:
        print("\nStarting DocTR process...\n")
        for image_path in images_to_test:
            ocr_with_doctr(image_path)
        print("--- All tests complete! ---")
    else:
        print("No images were found or selected.")