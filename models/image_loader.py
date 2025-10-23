import os
import tkinter as tk
from tkinter import filedialog

def get_images_from_folder():
    """
    Opens a dialog box for the user to select a folder.
    Scans that folder for image files and returns a list of their full paths.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    
    print("Please select the folder containing images to test...")
    folder_path = filedialog.askdirectory(title="Select Folder to Test")
    
    if not folder_path:
        print("No folder selected. Exiting.")
        return []  # Return an empty list if user cancels

    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    image_paths = []
    
    # Scan the selected folder for image files
    # Use sorted() to process files in a consistent order
    for filename in sorted(os.listdir(folder_path)):
        filepath = os.path.join(folder_path, filename)
        _ , extension = os.path.splitext(filename)
        
        # Check if it's a file and has a valid image extension
        if os.path.isfile(filepath) and extension.lower() in image_extensions:
            image_paths.append(filepath)
    
    print(f"\nFound {len(image_paths)} images to test in: {folder_path}")
    return image_paths