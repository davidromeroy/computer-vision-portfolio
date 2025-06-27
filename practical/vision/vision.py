import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, detection_conf=0.7, tracking_conf=0.5):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=detection_conf,
                                        min_tracking_confidence=tracking_conf)
        self.mp_draw = mp.solutions.drawing_utils
        self.cap = cv2.VideoCapture(0)

    def get_frame(self):
        success, frame = self.cap.read()
        if not success:
            return None, None
        frame = cv2.flip(frame, 1)
        return frame, self.hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    def draw_landmarks(self, frame, hand_landmarks):
        self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
