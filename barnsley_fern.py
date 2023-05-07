from PIL import Image, ImageDraw
import numpy as np
import os


Point = tuple[float, float]


def generate_stem(_, y: float) -> Point:
    return (0), (0.16 * y)


def generate_successive_ferns(x: float, y: float) -> Point:
    return (0.85 * x + 0.04 * y), (-0.04 * x + 0.85 * y + 1.6)


def generate_left_leaves(x: float, y: float) -> Point:
    return (0.2 * x - 0.26 * y), (0.23 * x + 0.22 * y + 1.6)


def generate_right_leaves(x: float, y: float) -> Point:
    return (-0.15 * x + 0.28 * y), (0.26 * x + 0.24 * y + 0.44)


def scale_point(x: float, y: float, width: int, height: int) -> Point:
    return ((x + 2.182) * (width - 1) / 4.8378), ((9.9983 - y) * (height - 1) / 9.9983)


FUNCTIONS: list = [
    generate_stem,
    generate_successive_ferns,
    generate_left_leaves,
    generate_right_leaves,
]

STARTING_POINT: tuple[int, int] = (0, 0)


x, y = STARTING_POINT
pixels = 1000
iterations = 100000
width, height = pixels, pixels

image = Image.new("RGB", (width, height), "black")
draw = ImageDraw.Draw(image)

for _ in range(iterations):
    function = np.random.choice(FUNCTIONS, p=[0.01, 0.85, 0.07, 0.07])
    x, y = function(x, y)
    scaled_x, scaled_y = scale_point(x, y, width, height)
    draw.point((scaled_x, scaled_y), "green")

image.show()

# Uncomment line 57-58 to save the image.
# os.makedirs("images", exist_ok=True)
# image.save("images/barnsley_fern.png", quality=95)
