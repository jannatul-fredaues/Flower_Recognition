# pip install --upgrade rembg onnxruntime pillow

import os
from rembg import remove
from PIL import Image

# Define input and output folder paths
input_folder = r"P:\Flower\Black_Cumin"
output_folder = r"P:\Flower\Black_Cumin_NoBG"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith((".png", ".jpg", ".jpeg")):  # Check file format
        input_path = os.path.join(input_folder, filename)
        # It's better to ensure the output file extension matches the format we plan to save as.
        # We will save as JPEG, so let's change the extension if needed.
        name, ext = os.path.splitext(filename)
        output_filename = name + ".jpg" # Force output to .jpg
        output_path = os.path.join(output_folder, output_filename)


        # Open the image and remove background
        with Image.open(input_path) as img:
            img_no_bg = remove(img)
            # Convert to RGB before saving as JPEG, as JPEG does not support alpha channel
            if img_no_bg.mode == 'RGBA':
                img_no_bg = img_no_bg.convert('RGB')
            img_no_bg.save(output_path, format="JPEG") # Ensure the format is JPEG

print("Background removal process completed successfully!")