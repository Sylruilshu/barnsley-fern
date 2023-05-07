from PIL import Image, ImageDraw
import numpy as np


def function_1(x, y):
    return (0 * x), (0.16 * y)


def function_2(x, y):
    return (0.85 * x + 0.04 * y), (-0.04 * x + 0.85 * y + 1.6)


def function_3(x, y):
    return (0.2 * x - 0.26 * y), (0.23 * x + 0.22 * y + 1.6)


def function_4(x, y):
    return (-0.15 * x + 0.28 * y), (0.26 * x + 0.24 * y + 0.44)


FUNCTIONS = [function_1, function_2, function_3, function_4]
X, Y = 0, 0

x, y = X, Y
pixels = 1000
iterations = 10000

width, height = pixels, pixels
image = Image.new("RGB", (width, height), "black")
draw = ImageDraw.Draw(image)

for _ in range(iterations):
    function = np.random.choice(FUNCTIONS, p=[0.01, 0.85, 0.07, 0.07])
    x, y = function(x, y)

    # draw.point(point, "green")
    # draw.point((point[0]+500, point[1]+500), "green")
    draw.point((x + 500, -y + 500), "green")

image.show()
