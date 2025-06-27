<<<<<<< HEAD
# 📄  Practical Project – OCR Invoices with EasyOCR

Este proyecto realiza reconocimiento óptico de caracteres (OCR) sobre facturas o documentos escaneados utilizando [EasyOCR](https://github.com/JaidedAI/EasyOCR). Fue desarrollado como parte de mi portafolio de visión por computadora.

## 🧠 Tecnologías
- Python 3.10+
- EasyOCR
- OpenCV
- Tesseract (en pruebas)
- Virtualenv
=======
# 📄 Practical Project –  Body-Controlled Games – Hand-Tracked Pong

This project allows you to play Pong using only your hand tracked in real time with a webcam. Built with **MediaPipe**, **OpenCV**, and **PyGame**, it's a scalable base for other body-controlled games.

## 🎯 Objective

- 🖐 Control the Pong paddle using hand movement.
- 🧠 Use MediaPipe to track hand position.
- 🕹️ Play a simplified version of Pong.
- 🧩 Modular structure to add more games and input modes later.
>>>>>>> e03aa41fdfe788461beb40fa39544840bf9ec145

## 📦 Requirements
- Python 3.9+
- pip

<<<<<<< HEAD
## 📁 Folder Structure

```
ocr-invoices-tesseract/
│
├── input/ # Imágenes de entrada
│ └── transferencia.jpg # Ejemplo de entrada
├── output/ # Archivos de texto con resultados
├── utils/
│ └── ocr_utils.py # Funciones OCR
├── main.py # Script principal
└── requirements.txt # Dependencias
```
=======
## 📁 Project Structure
```
vision-controller/
├── main.py                  ← Game launcher with menu
├── games/
│   ├── pong/
│   │   ├── game.py            ← Pong game logic
│   │   └── controller.py      ← Connect vision to paddle control
├── vision/
│   └── hand_tracker.py      ← MediaPipe hand tracking logic
├── assets/
│   └── demo_pong.gif         ← Demo recording or screenshots
├── requirements.txt
└── README.md
```

>>>>>>> e03aa41fdfe788461beb40fa39544840bf9ec145

## 🛠️ Installation Guide

<<<<<<< HEAD
## 🛠️ Installation Guide
Follow these steps to set up and run the face detection tool:

### 1. Clone the repository
```
git clone https://github.com/davidromeroy/computer-vision-portfolio.git
cd computer-vision-portfolio/intermediate/ocr-
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
└── your_image.jpg
```

## 5. Run the program
### Run example
```
python main.py input/transferencia.jpeg -o output/factura_text.txt
```

### Output example

```
Banco del Pueblo S.A.
Transferencia: $12.50
Fecha: 2024-11-03
Destinatario: Juan Pérez
...
```
---


## Autor
Hecho con ❤️ por David Romero Yánez


=======
Follow these steps to install and run the Pong demo:

### 1. Clone the repository

```bash
git clone https://github.com/davidromeroy/computer-vision-portfolio.git
cd computer-vision-portfolio/practical/
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

### 4. Run the program

```bash
python3 main.py
```
    
🖼 **Image mode with arguments:**

```bash
python3 main.py --input friends.png --mode detect
```

### 🎮 Controls
- Move your hand up and down in front of the webcam to control the paddle.
- Press ESC or close the window to quit.

### ✨ Future Extensions

- Add more games (Tetris, Brick Breaker, etc.)
- Control with full body using Pose estimation
- Detect custom gestures to perform game actions
- Run from browser using TensorFlow.js



## 📸 Demo

![Demo Pong](./assets/demo_pong.gif)

<!-- <h2>📸 Visual Results - Static Images</h2>
<table style="width:100%; table-layout: fixed;">
  <thead>
    <tr>
      <th style="text-align:center;">Original</th>
      <th style="text-align:center;">Detection</th>
      <th style="text-align:center;">Blur</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="./media/friends.png" style="width:250px; height:200px; object-fit:cover;"/></td>
      <td><img src="./media/detected_friends.png" style="width:250px; height:200px; object-fit:cover;"/></td>
      <td><img src="./media/blurred_friends.png" style="width:250px; height:200px; object-fit:cover;"/></td>
    </tr>
    <tr>
      <td><img src="./media/graduationIA.png" style="width:250px; height:200px; object-fit:cover;"/></td>
      <td><img src="./media/detected_graduationIA.png" style="width:250px; height:200px; object-fit:cover;"/></td>
      <td><img src="./media/blurred_graduationIA.png" style="width:250px; height:200px; object-fit:cover;"/></td>
    </tr>
    <tr>
      <td><img src="./media/meeting.png" style="width:250px; height:200px; object-fit:cover;"/></td>
      <td><img src="./media/detected_meeting.png" style="width:250px; height:200px; object-fit:cover;"/></td>
      <td><img src="./media/blurred_meeting.png" style="width:250px; height:200px; object-fit:cover;"/></td>
    </tr>
  </tbody>
</table>




<h2>🎥 Results - Captures from Webcam</h2>

<table style="width:100%; table-layout: fixed;">
  <thead>
    <tr>
      <th style="text-align:center;">Original Webcam</th>
      <th style="text-align:center;">Detection</th>
      <th style="text-align:center;">Blur</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="./media/webcam_original.png" style="width:100%; max-width:250px; object-fit:cover;"></td>
      <td><img src="./media/webcam_detected.png" style="width:100%; max-width:250px; object-fit:cover;"></td>
      <td><img src="./media/webcam_blurred.png" style="width:100%; max-width:250px; object-fit:cover;"></td>
    </tr>
  </tbody>
</table>
-->


## 🧑‍💻 Autor
David Romero Yánez
>>>>>>> e03aa41fdfe788461beb40fa39544840bf9ec145
