# 📄  Practical Project – OCR Invoices with EasyOCR

Este proyecto realiza reconocimiento óptico de caracteres (OCR) sobre facturas o documentos escaneados utilizando [EasyOCR](https://github.com/JaidedAI/EasyOCR). Fue desarrollado como parte de mi portafolio de visión por computadora.

## 🧠 Tecnologías
- Python 3.10+
- EasyOCR
- OpenCV
- Tesseract (en pruebas)
- Virtualenv

---

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

---

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


