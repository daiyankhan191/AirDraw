from hand_tracker import HandTracker
from gesture_utils import detect_gesture
from drawer import Canvas
import cv2

cap = cv2.VideoCapture(0)
tracker = HandTracker()
canvas = Canvas()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    landmarks, frame = tracker.find_hand(frame)

    if landmarks:
        gesture = detect_gesture(landmarks)
        canvas.update(landmarks, gesture)

    output = canvas.overlay(frame)
    cv2.imshow("AirDraw", output)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
