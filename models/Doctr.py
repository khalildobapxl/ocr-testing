from doctr.io import DocumentFile
from doctr.models import ocr_predictor, from_hub
import cv2
import numpy as np
import os
from image_loader import get_images_from_folder  # <-- IMPORT YOUR FUNCTION

# This gets the directory where your script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# --- 1. Initialize the OCR Predictor ---
print("Loading DocTR model...")
det_model = from_hub("Felix92/doctr-torch-db-mobilenet-v3-large")
rec_model = from_hub("Felix92/doctr-torch-parseq-multilingual-v1")
model = ocr_predictor(det_arch=det_model, reco_arch=rec_model, pretrained=True)
print("Model loaded.")


def ocr_with_doctr(image_path, save_visualized=True, output_dir="output"):
    """
    Performs OCR on an image file using DocTR and optionally saves visualization.
    """
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' was not found.")
        return

    # Create output directory if it doesn't exist
    if save_visualized and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = os.path.basename(image_path)
    print(f"Analyzing {filename}...")
    
    try:
        # --- 2. Load the image and Document ---
        doc = DocumentFile.from_images(image_path)
        # Load image with OpenCV for drawing
        image = cv2.imread(image_path)
        height, width = image.shape[:2]

        # --- 3. Run the prediction ---
        print("Running DocTR model...")
        result = model(doc)

        # --- 4. Process and Display Results ---
        print(f"\n--- DocTR Output for {filename} ---")
        
        if not result.pages:
            print("  No pages or text found in document.")
            print("-" * (len(filename) + 21) + "\n")
            return

        for page in result.pages:
            for block in page.blocks:
                for line in block.lines:
                    for word in line.words:
                        # Get word text and confidence
                        print(f"  Text: {word.value} | Confidence: {word.confidence:.4f}")

                        # Only draw boxes if we are saving the image
                        if save_visualized:
                            geometry = word.geometry
                            # Convert normalized coordinates to pixel coordinates
                            x1 = int(geometry[0][0] * width)
                            y1 = int(geometry[0][1] * height)
                            x2 = int(geometry[1][0] * width)
                            y2 = int(geometry[1][1] * height)

                            # Draw rectangle on image
                            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                            # Add text label
                            label = f"{word.value} ({word.confidence:.2f})"
                            cv2.putText(
                                image, label, (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1
                            )

        print("-" * (len(filename) + 21) + "\n")

        # --- 5. Save the visualized image ---
        if save_visualized:
            output_path = os.path.join(output_dir, f"boxed_{filename}")
            cv2.imwrite(output_path, image)
            print(f"Saved visualization to: {output_path}")
            print("------------------------------------------\n")

    except Exception as e:
        print(f"An error occurred while processing {filename}: {e}\n")


# --- THIS IS THE MODIFIED SECTION ---
if __name__ == "__main__":
    
    # 1. Call the function to let the user choose a folder
    images_to_test = get_images_from_folder()
    
    # 2. Run the tests ONLY on the list of images it returned
    if images_to_test:
        print("\nStarting DocTR process...\n")
        
        # Define the output directory (e.g., a folder named "output"
        # right next to your script)
        output_dir = os.path.join(SCRIPT_DIR, "output")
        
        for image_path in images_to_test:
            # Call the function with the save parameters
            ocr_with_doctr(
                image_path,
                save_visualized=True,
                output_dir=output_dir
            )
            
        print("--- All tests complete! ---")
    else:
        print("No images were found or selected.")