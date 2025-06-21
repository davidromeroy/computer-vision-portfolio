# main.py

import argparse
import os
from utils.ocr_utils import *

# def prompt_action():
#     while True:
#         print("\n¿Qué acción deseas realizar?")
#         print("0. Salir")
#         print("1. Detectar rostros")
#         print("2. Difuminar rostros")
#         choice = input("Selecciona (0, 1 o 2): ").strip()

#         match choice:
#             case "1":
#                 return "detect"
#             case "2":
#                 return "blur"
#             case "0":
#                 print("👋 Saliendo del programa.")
#                 exit()
#             case _:
#                 print("❌ Opción inválida. Intenta de nuevo.")

image_path = "input/transferencia.jpeg"
output_path = "output/factura1_text.txt"

texto = extract_text_easyocr(image_path)
print(texto)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(texto)
