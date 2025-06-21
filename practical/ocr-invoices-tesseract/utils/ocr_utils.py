# ocr_utils.py

import cv2
import easyocr
import os

def extract_text_easyocr(image_path, lang='es'):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"No se encontró la imagen: {image_path}")

    reader = easyocr.Reader([lang])
    results = reader.readtext(image_path)

    text_lines = []
    for bbox, text, confidence in results:
        if confidence > 0.5:  # Puedes ajustar este umbral
            text_lines.append(text)

    return "\n".join(text_lines)

def show_image_with_boxes(image_path, lang='es'):
    image = cv2.imread(image_path)
    reader = easyocr.Reader([lang])
    results = reader.readtext(image_path)

    for bbox, text, confidence in results:
        if confidence > 0.5:
            pts = [tuple(map(int, point)) for point in bbox]
            cv2.polylines(image, [np.array(pts)], isClosed=True, color=(0, 255, 0), thickness=2)
            cv2.putText(image, text, pts[0], cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow("Texto detectado", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

