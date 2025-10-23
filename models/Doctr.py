from doctr.io import DocumentFile
from doctr.models import ocr_predictor, from_hub
import cv2
import numpy as np
import os
from _images import all_images

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

    # --- 2. Load the image as a Document ---
    doc = DocumentFile.from_images(image_path)

    # Load image with OpenCV for drawing
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    # --- 3. Run the prediction ---
    print("Analyzing document...")
    result = model(doc)

    # --- 4. Process and Display Results ---
    print(f"\n--- DocTR Output for {image_path} ---")
    for page in result.pages:
        for block in page.blocks:
            for line in block.lines:
                for word in line.words:
                    # Get word text and confidence
                    print(f"Text: {word.value} | Confidence: {word.confidence:.4f}")

                    # Get bounding box coordinates (normalized 0-1)
                    # DocTR geometry: ((xmin, ymin), (xmax, ymax))
                    geometry = word.geometry

                    # Convert normalized coordinates to pixel coordinates
                    x1 = int(geometry[0][0] * width)
                    y1 = int(geometry[0][1] * height)
                    x2 = int(geometry[1][0] * width)
                    y2 = int(geometry[1][1] * height)

                    # Draw rectangle on image
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    # Add text label with confidence
                    label = f"{word.value} ({word.confidence:.2f})"
                    cv2.putText(
                        image,
                        label,
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 0, 255),
                        1,
                    )

    print("------------------------------------------")

    # --- 5. Save the visualized image ---
    if save_visualized:
        output_path = os.path.join(output_dir, f"boxed_{os.path.basename(image_path)}")
        cv2.imwrite(output_path, image)
        print(f"Saved visualization to: {output_path}")

    print("------------------------------------------")


if __name__ == "__main__":
    for image_path in all_images:
        ocr_with_doctr(
            image_path,
            save_visualized=True,
            output_dir=os.path.join(SCRIPT_DIR, "output"),
        )
