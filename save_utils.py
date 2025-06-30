import cv2
import datetime

def save_canvas(canvas):
    filename = f"airdraw_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    cv2.imwrite(filename, canvas)
    return filename
