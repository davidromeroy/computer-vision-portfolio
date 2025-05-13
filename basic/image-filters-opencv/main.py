import cv2
import os
import argparse
from filters import *

# Argument parser setup
# Allows the user to provide an image path as an input argument
parser = argparse.ArgumentParser(description="Apply basic image filters using OpenCV.")
parser.add_argument('--input', type=str, default="input/sample.jpg", help="Path to the input image")
args = parser.parse_args()

# Load the input image
img_path = args.input
img = cv2.imread(img_path)

if img is None:
    print(f"❌ Image not found at path: {img_path}")
    exit()

# Create output directory if it doesn't exist
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Apply and save each filter
cv2.imwrite(f"{OUTPUT_DIR}/gray.jpg", apply_grayscale(img))
cv2.imwrite(f"{OUTPUT_DIR}/blur.jpg", apply_blur(img))
cv2.imwrite(f"{OUTPUT_DIR}/edges.jpg", apply_canny(img))
cv2.imwrite(f"{OUTPUT_DIR}/threshold.jpg", apply_threshold(img))
cv2.imwrite(f"{OUTPUT_DIR}/laplacian.jpg", apply_laplacian(img))
cv2.imwrite(f"{OUTPUT_DIR}/histogram_equalized.jpg", apply_equalize_histogram(img))

print("✅ All filters applied and images saved in the 'output' folder.")

#TODO: use environments