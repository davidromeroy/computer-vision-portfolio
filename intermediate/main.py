# main.py

import argparse
import os
from utils.face_utils import *

def prompt_action():
    while True:
        print("\n¿Qué acción deseas realizar?")
        print("0. Salir")
        print("1. Detectar rostros")
        print("2. Difuminar rostros")
        choice = input("Selecciona (0, 1 o 2): ").strip()

        match choice:
            case "1":
                return "detect"
            case "2":
                return "blur"
            case "0":
                print("👋 Saliendo del programa.")
                exit()
            case _:
                print("❌ Opción inválida. Intenta de nuevo.")

def main():
    # Create output folder if it does not exist
    os.makedirs("output", exist_ok=True)
    parser = argparse.ArgumentParser(description="Face Detection/Blurring using MediaPipe")
    parser.add_argument('--input', type=str, help="Nombre de imagen en carpeta 'input/' o 'webcam'")
    parser.add_argument('--mode', type=str, choices=["detect", "blur"], help="Acción a realizar: 'detect' o 'blur'")

    args = parser.parse_args()
    name_image = args.input
    mode = args.mode

    # Si no se pasa ningún input, pedir por consola
    if not name_image:
        name_image = input("🖼️ Ingresa el nombre de la imagen (debe estar en la carpeta 'input/') o escribe 'webcam' para usar la cámara: ").strip()    
    #Ruta completa a la imagen (si no es webcam)
    input_source = name_image if name_image.lower() == "webcam" else os.path.join("input", name_image)

    
    # Webcam
    if input_source.lower() == "webcam":
        if not mode:
            mode = prompt_action()
        print(f"[INFO] Iniciando webcam con modo: {mode.upper()}")

        if mode == "blur":
            blurred_faces_from_webcam()
        else:
            detect_faces_from_webcam()
        return
    
    # Imagen local
    if not os.path.exists(input_source):
        print(f"[ERROR] Ruta '{input_source}' no encontrada.")
        return

    if not mode:
        mode = prompt_action()

    print(f"[INFO] Procesando '{input_source}' en modo: {mode.upper()}")
    base_name, _ = os.path.splitext(os.path.basename(name_image))

    try:
        if mode == "blur":
            blurred = blur_faces(input_source)
            show_image(blurred, title="Rostros Difuminados")
            save_output(blurred, f"blurred_{base_name}.jpg")
        else:
            image_with_faces, detections = detect_faces_with_ids(input_source)
            print(f"🔍 Detecciones: {len(detections)}")
            show_image(image_with_faces, "Rostros Detectados")
            save_output(image_with_faces, f"detected_{base_name}.jpg")
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()
