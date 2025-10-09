from doctr.io import DocumentFile
from doctr.models import ocr_predictor
import os
from _images import all_images

# --- 1. Initialize the OCR Predictor ---
print("Loading DocTR model...")
model = ocr_predictor(pretrained=True)
print("Model loaded.")


def ocr_with_doctr(image_path):
    """
    Performs OCR on an image file using DocTR and prints the results.
    """
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' was not found.")
        return

    
    # --- 2. Load the image as a Document ---
    doc = DocumentFile.from_images(image_path)
    
    # --- 3. Run the prediction ---
    print("Analyzing document...")
    result = model(doc)

    # --- 4. Process and Display Results ---
    print(f"\n--- DocTR Output for {image_path} ---")
    for page in result.pages:
        for block in page.blocks:
            for line in block.lines:
                # Reconstruct the line from individual words
                line_text = ' '.join([word.value for word in line.words])
                confidence = min([word.confidence for word in line.words]) if line.words else 0
                print(f"Text: {line_text} | Min Confidence: {confidence:.4f}")

    print("------------------------------------------")


if __name__ == "__main__":
    for image_path in all_images:
        ocr_with_doctr(image_path)