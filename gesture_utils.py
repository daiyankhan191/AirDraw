import math

def distance(p1, p2):
    return math.hypot(p1[1] - p2[1], p1[2] - p2[2])

def detect_gesture(landmarks):
    if not landmarks:
        return None

    fingers_up = []

    # Thumb
    fingers_up.append(landmarks[4][1] < landmarks[3][1])  # x comparison
    # Fingers
    for tip in [8, 12, 16, 20]:
        fingers_up.append(landmarks[tip][2] < landmarks[tip - 2][2])  # y comparison

    if fingers_up == [False, True, True, False, False]:  # Index + Middle
        return 'color_picker'
    elif all(not f for f in fingers_up):  # All down = fist
        return 'clear'
    elif distance(landmarks[4], landmarks[8]) < 40:  # Thumb and index close
        return 'change_brush'

    return 'draw'
