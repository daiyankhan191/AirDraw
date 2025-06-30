import streamlit as st
import cv2
import numpy as np
from hand_tracker import HandTracker
from gesture_utils import detect_gesture
from drawer import Canvas
from save_utils import save_canvas

st.set_page_config(page_title="AirDraw", layout="wide")
st.title("🖐️ AirDraw – Draw with Your Hand")

run_app = st.button("Start Drawing")
save_triggered = st.button("💾 Save Drawing")

FRAME_WINDOW = st.image([])

if run_app:
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    canvas = Canvas()

    stop = False
    while not stop:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        landmarks, frame = tracker.find_hand(frame)

        if landmarks:
            gesture = detect_gesture(landmarks)
            canvas.update(landmarks, gesture)

        output = canvas.overlay(frame)
        FRAME_WINDOW.image(output, channels="BGR")

        # Save image
        if save_triggered:
            saved_file = save_canvas(canvas.canvas)
            st.success(f"Saved as {saved_file}")
            save_triggered = False
            stop = True  # Exit the loop after saving

    cap.release()
else:
    st.info("Tick the box above to start drawing.")
