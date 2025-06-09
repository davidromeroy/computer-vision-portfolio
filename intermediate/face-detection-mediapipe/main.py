# main.py

import argparse
import os
from utils.face_utils import *

def main():
    # Create output folder if it does not exist
    os.makedirs("output", exist_ok=True)
    parser = argparse.ArgumentParser(description="Face Detection using MediaPipe")
    parser.add_argument('--input', type=str, required=True,
                        help="Path to input image or 'webcam' for live detection")

    args = parser.parse_args()
    input_source = args.input

    if input_source.lower() == 'webcam':
        print("[INFO] Starting webcam face detection...")
        # detect_faces_from_webcam() TODO: poner por parametros si hacer blurred o detected
        blurred_faces_from_webcam()
    else:
        if not os.path.exists(input_source):
            print(f"[ERROR] Image path '{input_source}' not found.")
            return

        try:
            blurred = blur_faces(input_source)
            show_image(blurred, title="Unfocused Faces")
            # print("Image blurred successfully")

            image_with_faces, detections = detect_faces_with_ids(input_source)
            print(f"🔍 Detecciones: {len(detections)}")
            show_image(image_with_faces, "Detected Faces")
            save_output(image_with_faces, "detected_faces.jpg")
        except FileNotFoundError as e:
                print(e)

if __name__ == "__main__":
    main()
