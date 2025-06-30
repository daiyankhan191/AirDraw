import numpy as np
import cv2
import config

class Canvas:
    def __init__(self, w=640, h=480, bg=None):
        if bg is not None:
            self.canvas = bg.copy()
        else:
            self.canvas = np.zeros((h, w, 3), dtype=np.uint8)
        self.prev_point = None
        self.brush_color = config.DEFAULT_COLOR
        self.brush_size = config.DEFAULT_SIZE

    def update(self, landmarks, gesture):
        x, y = landmarks[8][1], landmarks[8][2]  # Index tip

        if gesture == 'clear':
            self.canvas[:] = (255, 255, 255)  # White background
        elif gesture == 'color_picker':
            self.brush_color = config.next_color(self.brush_color)
        elif gesture == 'change_brush':
            self.brush_size = config.next_brush_size(self.brush_size)
        elif gesture == 'draw':
            if self.prev_point:
                cv2.line(self.canvas, self.prev_point, (x, y), self.brush_color, self.brush_size)
            self.prev_point = (x, y)
        else:
            self.prev_point = None

    def overlay(self, frame):
        return cv2.addWeighted(frame, 0.5, self.canvas, 0.5, 0)
