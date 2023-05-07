from PIL import Image, ImageDraw
import numpy as np


def transform_point(x, y, a, b, c, d, e, f):
    return (a * x + b * y + e), (c * x + d * y + f)


def determine_transformation(collection: dict[dict], key: str, index: int):
    affine_transformations = collection[key]
    affine_transformation = affine_transformations[index]

    a = affine_transformation[0]
    b = affine_transformation[1]
    c = affine_transformation[2]
    d = affine_transformation[3]
    e = affine_transformation[4]
    f = affine_transformation[5]

    return a, b, c, d, e, f


def determine_probabilities(collection_probabilities: dict, key: str):
    probabilities = collection_probabilities[key]
    return probabilities


TRANSFORMATION_INDEXES = [1, 2, 3, 4]


AFFINE_TRANSFORMATIONS_VALUES = {
    "barnsley-fern": {
        1: [0, 0, 0, 0.16, 0, 0],
        2: [0.85, 0.04, -0.04, 0.85, 0, 1.6],
        3: [0.2, -0.26, 0.23, 0.22, 0, 1.6],
        4: [-0.15, 0.28, 0.26, 0.24, 0, 0.44],
    },
    "alt-barnsley-fern": {
        1: [0, 0, 0, 0.2, 0, -0.12],
        2: [0.845, 0.035, -0.035, 0.82, 0, 1.6],
        3: [0.2, -0.31, 0.255, 0.245, 0, 0.29],
        4: [-0.15, 0.24, 0.25, 0.2, 0, 0.68],
    },
    "culcita": {
        1: [0, 0, 0, 0.25, 0, -0.14],
        2: [0.85, 0.02, -0.02, 0.83, 0, 1],
        3: [0.09, -0.28, 0.3, 0.11, 0, 0.6],
        4: [-0.09, 0.28, 0.3, 0.09, 0, 0.7],
    },
    "cyclosorus": {
        1: [0, 0, 0, 0.25, 0, -0.4],
        2: [0.95, 0.005, -0.005, 0.93, -0.002, 0.5],
        3: [0.035, -0.2, 0.16, 0.04, -0.09, 0.02],
        4: [-0.04, 0.2, 0.16, 0.04, 0.083, 0.12],
    },
    "fishbone": {
        1: [0, 0, 0, 0.25, 0, -0.4],
        2: [0.95, 0.002, -0.002, 0.93, -0.002, 0.5],
        3: [0.035, -0.11, 0.27, 0.01, -0.05, 0.005],
        4: [-0.04, 0.11, 0.27, 0.01, 0.047, 0.06],
    },
    "fractal-tree": {
        1: [0, 0, 0, 0.5, 0, 0],
        2: [0.42, -0.42, 0.42, 0.42, 0, 0.2],
        3: [0.42, 0.42, -0.42, 0.42, 0, 0.2],
        4: [0.1, 0, 0, 0.1, 0, 0.2],
    },
    "golden-bee": {
        1: [0.6178, 0, 0, -0.6178, 0, 1],
        2: [0, -0.786, 0.786, 0, 0.786, 0],
        3: [0, 0, 0, 0, 0, 0],
        4: [0, 0, 0, 0, 0, 0],
    },
}

PROBABILITIES = {
    "barnsley-fern": [0.01, 0.85, 0.07, 0.07],
    "alt-barnsley-fern": [0.01, 0.85, 0.07, 0.07],
    "culcita": [0.02, 0.84, 0.07, 0.07],
    "cyclosorus": [0.02, 0.84, 0.07, 0.07],
    "fishbone": [0.02, 0.84, 0.07, 0.07],
    "fractal-tree": [0.05, 0.4, 0.4, 0.15],
    "golden-bee": [0.5, 0.5, 0, 0],
}


# Fractal tree
# scaled_x = (x + 0.25) * (width) * 2
# scaled_y = (0.5 - y) * (height) * 2

# Golden bee
# scaled_x = (x) * (width * 1.275)
# scaled_y = (1 - y) * (height)

# Barnsley fern
# scaled_x = (x + 2.182) * (width - 1) / 4.8378
# scaled_y = (9.9983 - y) * (height - 1) / 9.9983

# Culcita
# scaled_x = (x + 2) * (width) / 4
# scaled_y = (5.8 - y) * (height) / 6

# Cyclosorus
# scaled_x = (x + 2.5) * (width) / 5
# scaled_y = (7.105 - y) * (height) / 7.675


# STARTING_POINT = (0, 0)
X, Y = 0, 0


pixels = 5000
iterations = 10000000

# pixels = 1000
# iterations = 100000

width, height = pixels, pixels
image = Image.new("RGB", (width, height), "black")
draw = ImageDraw.Draw(image)

x, y = X, Y

key = "fishbone"

probabilities = determine_probabilities(PROBABILITIES, key)

for _ in range(iterations):
    index = np.random.choice(TRANSFORMATION_INDEXES, p=probabilities)

    a, b, c, d, e, f = determine_transformation(
        AFFINE_TRANSFORMATIONS_VALUES, key, index
    )

    x, y = transform_point(x, y, a, b, c, d, e, f)

    # scaled_x = (x + 2.182) * (width) / 4.8378
    scaled_x = (x + 2.5) * (width) / 5
    scaled_y = (7.105 - y) * (height) / 7.675

    draw.point((scaled_x, scaled_y), "#e0d7c6")

image.show()
# image.save(f"images/{key}/{key}.png", quality=95)
