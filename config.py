DEFAULT_COLOR = (255, 0, 0)
DEFAULT_SIZE = 5

COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
SIZES = [3, 5, 7, 10]

def next_color(current):
    index = COLORS.index(current)
    return COLORS[(index + 1) % len(COLORS)]

def next_brush_size(current):
    index = SIZES.index(current)
    return SIZES[(index + 1) % len(SIZES)]
