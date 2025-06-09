# utils/face_utils.py

import cv2
import matplotlib.pyplot as plt
import mediapipe as mp

# Global initializers
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Function to show an image using matplotlib
def show_image(image, title="Image"):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(8, 6))
    plt.imshow(rgb)
    plt.title(title)
    plt.axis("off")
    plt.show()

# Function to resize an image while maintaining aspect ratio
def resize_image(image, width=800):
    h, w = image.shape[:2]
    height = int(h * (width / w))
    return cv2.resize(image, (width, height))

# Function to save the output image
def save_output(image, filename="output.jpg", folder="output"):
    path = f"{folder}/{filename}"
    cv2.imwrite(path, image)
    print(f"✅ Image saved in: {path}")


# Function to detect faces and print detection scores
def detect_faces_with_ids(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"❌ Unable to load image: {image_path}")
    
    image = resize_image(image)
    detections_data = []

    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as detector:
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = detector.process(rgb)

        if not results.detections:
            print("❌ No faces detected.")
            return image, []

        for i, detection in enumerate(results.detections):
            bbox = detection.location_data.relative_bounding_box
            h, w, _ = image.shape
            rect_start = int(bbox.xmin * w), int(bbox.ymin * h)
            rect_end = int((bbox.xmin + bbox.width) * w), int((bbox.ymin + bbox.height) * h)
            score = detection.score[0]

            mp_drawing.draw_detection(image, detection)
            cv2.putText(image, f"ID: {i}", rect_start, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            detections_data.append(((rect_start, rect_end), score))

    return image, detections_data

# Function to blur faces in an image
def blur_faces(image_path):
    image = cv2.imread(image_path)
    image = resize_image(image)  # Resize the image for better visualization
    if image is None:
        raise FileNotFoundError(f"Unable to load image: {image_path}")

    output = image.copy()
    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as detector:
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = detector.process(rgb)

        if results.detections:
            h, w, _ = image.shape
            for i, detection in enumerate(results.detections):
                bbox = detection.location_data.relative_bounding_box
                x1 = int(bbox.xmin * w)
                y1 = int(bbox.ymin * h)
                x2 = int((bbox.xmin + bbox.width) * w)
                y2 = int((bbox.ymin + bbox.height) * h)

                face_roi = output[y1:y2, x1:x2]
                face_blur = cv2.GaussianBlur(face_roi, (55, 55), 30)
                output[y1:y2, x1:x2] = face_blur
        else:
            print("⚠️ No faces were detected for defocusing.")
            return None

    return output


# Function to detect faces in real-time from webcam
def detect_faces_from_webcam():
    cap = cv2.VideoCapture(0)

    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as detector:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = detector.process(rgb)

            if results.detections:
                h, w, _ = frame.shape  # Height and width to convert relative bboxes

                for i, detection in enumerate(results.detections):
                    bbox = detection.location_data.relative_bounding_box
                    score = detection.score[0]
                    x = int(bbox.xmin * w)
                    y = int(bbox.ymin * h)

                    #print(f"[#{i+1}] Confidence: {score:.2f}, BBox: (x={bbox.xmin:.2f}, y={bbox.ymin:.2f}, w={bbox.width:.2f}, h={bbox.height:.2f})")
                    mp_drawing.draw_detection(frame, detection)

                    # Draw ID as text
                    cv2.putText(frame, f"#{i+1}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                                0.9, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.imshow('Face Detection - Press ESC to exit', frame)
            if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
                break

    cap.release()
    cv2.destroyAllWindows()

# Function to blur faces from webcam in real-time
def blurred_faces_from_webcam():
    cap = cv2.VideoCapture(0)

    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as detector:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = detector.process(rgb)

            if results.detections:
                h, w, _ = frame.shape  # Height and width to convert relative bboxes
                for i, detection in enumerate(results.detections):
                    bbox = detection.location_data.relative_bounding_box
                    x1 = int(bbox.xmin * w)
                    y1 = int(bbox.ymin * h)
                    x2 = int((bbox.xmin + bbox.width) * w)
                    y2 = int((bbox.ymin + bbox.height) * h)

                    face_roi = frame[y1:y2, x1:x2]
                    face_blur = cv2.GaussianBlur(face_roi, (55, 55), 30)
                    frame[y1:y2, x1:x2] = face_blur

            cv2.imshow('Blurred face - Press ESC to exit', frame)
            if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
                break

    cap.release()
    cv2.destroyAllWindows()
