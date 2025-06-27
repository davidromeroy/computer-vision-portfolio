import sys
import cv2
from games import game
from vision import vision

def main():
    hand_tracker = vision.HandTracker()
    paddle_game = game.PaddleGame()

    print("Modo de jugador 2:")
    print("1. Automático")
    print("2. Controlado por segunda mano")
    opcion = input("Selecciona una opción (1 o 2): ")
    if opcion == "2":
        paddle_game.mode_player2 = "hand"
    else:
        paddle_game.mode_player2 = "auto"

    running = True
    while running:
        frame, results = hand_tracker.get_frame()
        if frame is None:
            break

        # Control jugador 1 (mano izquierda)
        if results and results.multi_hand_landmarks:
            hand1 = results.multi_hand_landmarks[0]
            hand_tracker.draw_landmarks(frame, hand1)
            y_norm_1 = hand1.landmark[0].y
            new_paddle1_y = int(y_norm_1 * paddle_game.height) - paddle_game.paddle_height // 2
            paddle_game.update_paddle_y(new_paddle1_y)

            # Control jugador 2 (si modo = hand y hay segunda mano)
            if paddle_game.mode_player2 == "hand" and len(results.multi_hand_landmarks) > 1:
                hand2 = results.multi_hand_landmarks[1]
                hand_tracker.draw_landmarks(frame, hand2)
                y_norm_2 = hand2.landmark[0].y
                new_paddle2_y = int(y_norm_2 * paddle_game.height) - paddle_game.paddle_height // 2
                paddle_game.paddle2_y = max(0, min(new_paddle2_y, paddle_game.height - paddle_game.paddle_height))

        # Actualizar lógica
        paddle_game.update_ball()
        if paddle_game.mode_player2 == "auto":
            paddle_game.update_ai_paddle()

        # Dibujar y actualizar
        running = paddle_game.handle_events()
        paddle_game.draw()
        paddle_game.tick()

        # Mostrar cámara con landmarks
        cv2.imshow("Camara", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC para salir
            break

    hand_tracker.release()
    paddle_game.quit()
    sys.exit()

if __name__ == "__main__":
    main()
