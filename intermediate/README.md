# 🟡 Intermediate Project – Face Detection with MediaPipe

This project demonstrates real-time face detection using Google's MediaPipe framework, integrating it with OpenCV for video capture and visualization.

## 🎯 Objective

- Detect faces in images and live video streams using MediaPipe
- Practice modular, clean Python scripting
- Support image and webcam input via command-line arguments
- Provide visual results with annotated outputs and GIF demos

## 📂 Folder Structure

face-detection-mediapipe/
├── main.py               ← Entrada principal
├── requirements.txt      ← Lista de dependencias
├── input/                ← Imágenes a procesar
│   ├── sample.jpg
├── output/               ← Imágenes procesadas
│   ├── detected_sample.jpg
├── assets/               ← Archivos para el README (GIFs, etc.)
│   ├── input_image.jpg
│   ├── output_image.jpg
│   └── demo_video.gif
└── utils/
    └── face_utils.py     ← Lógica de detección facial


## 🧪 Features Available

- `detect_faces_image`: Detects and annotates faces on static images  
- `detect_faces_video`: Performs real-time detection from webcam or video  
- `draw_detections`: Draws bounding boxes and confidence scores  
- `save_output`: Saves annotated results to `output/` folder  
- `--input`: Accepts a file path or `webcam` mode from CLI  

## 🛠️ Installation Guide

Follow these steps to set up and run the face detection tool:

### 1. Clone the repository

```bash
git clone https://github.com/davidromeroy/computer-vision-portfolio.git
cd computer-vision-portfolio/intermediate/face-detection-mediapipe
```

### 2. Create and activate a virtual environment

On windows:
```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Add input images
Place your image(s) inside the `input/` folder. For example:


```bash
input/
└── your_face_image.jpg
```
### 5. Run the program
To run on a static image:

```bash
python main.py --input input/your_face_image.jpg
```

To run on your webcam:

```bash
python main.py --input webcam
```

### 6. Output
Annotated image/video frames will be saved in the `output/` folder.

## 🖼️ Outputs


### ✅ Example Image Input & Output

| Original | Input | Output |
|----------|-----------|---------------|
| ![Original] | ![Gray] | ![Blur] |

### 🎥 Live Demo (Webcam)


## 🛠️ Tech Stack
- Python 3.11+

- OpenCV

- MediaPipe

- Numpy

- Argparse (for CLI)

- Jupyter Notebook (optional for visual exploration)
