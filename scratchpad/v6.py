from PIL import Image, ImageDraw
import numpy as np


def generate_stem(x, y, a, b, c, d, e, f):
    return (a * x + b * y + e), (c * x + d * y + f)


def generate_successive_ferns(x, y, a, b, c, d, e, f):
    return (a * x + b * y + e), (c * x + d * y + f)


def generate_left_leaves(x, y, a, b, c, d, e, f):
    return (a * x + b * y + e), (c * x + d * y + f)


def generate_right_leaves(x, y, a, b, c, d, e, f):
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


FUNCTIONS = [
    generate_stem,
    generate_successive_ferns,
    generate_left_leaves,
    generate_right_leaves,
]

AFFINE_TRANSFORMATIONS_VALUES = {
    "barnsley fern": {
        1: [0, 0, 0, 0.16, 0, 0],
        2: [0.85, 0.04, -0.04, 0.85, 0, 1.6],
        3: [0.2, -0.26, 0.23, 0.22, 0, 1.6],
        4: [-0.15, 0.28, 0.26, 0.24, 0, 0.44],
    },
    "alt barnsley fern": {
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
        1: [0, 0, 0, 0.16, 0, 0],
        2: [0.85, 0.04, -0.04, 0.85, 0, 1.6],
        3: [0.2, -0.26, 0.23, 0.22, 0, 1.6],
        4: [-0.15, 0.28, 0.26, 0.24, 0, 0.44],
    },
    "fishbone": {
        1: [0, 0, 0, 0.25, 0, -0.4],
        2: [0.95, 0.002, -0.002, 0.93, -0.002, 0.5],
        3: [0.035, -0.11, 0.27, 0.01, -0.05, 0.005],
        4: [-0.04, 0.11, 0.27, 0.01, 0.047, 0.06],
    },
    "fractal tree": {
        1: [0, 0, 0, 0.5, 0, 0],
        2: [0.42, -0.42, 0.42, 0.42, 0, 0.2],
        3: [0.42, 0.42, -0.42, 0.42, 0, 0.2],
        4: [0.1, 0, 0, 0.1, 0, 0.2],
    },
    "golden bee": {
        1: [0.6178, 0, 0, -0.6178, 0, 1],
        2: [0, -0.786, 0.786, 0, 0.786, 0],
        3: [0, 0, 0, 0, 0, 0],
        4: [0, 0, 0, 0, 0, 0],
    },
}

PROBABILITIES = {
    "barnsley fern": [0.01, 0.85, 0.07, 0.07],
    "alt barnsley fern": [0.01, 0.85, 0.07, 0.07],
    "culcita": [0.02, 0.84, 0.07, 0.07],
    "cyclosorus": [0.02, 0.84, 0.07, 0.07],
    "fishbone": [0.02, 0.84, 0.07, 0.07],
    "fractal tree": [0.05, 0.4, 0.4, 0.15],
    "golden bee": [0.5, 0.5, 0, 0],
}

# STARTING_POINT = (0, 0)
X, Y = 0, 0


pixels = 1000
iterations = 5000

# pixels = 5000
# iterations = 10000000

width, height = pixels, pixels
image = Image.new("RGB", (width, height), "black")
draw = ImageDraw.Draw(image)

# point = STARTING_POINT
x, y = X, Y

key = "alt barnsley fern"

probabilities = determine_probabilities(PROBABILITIES, key)

for _ in range(iterations):
    function = np.random.choice(FUNCTIONS, p=probabilities)
    if function == generate_stem:
        index = 1
    if function == generate_successive_ferns:
        index = 2
    if function == generate_left_leaves:
        index = 3
    if function == generate_right_leaves:
        index = 4

    a, b, c, d, e, f = determine_transformation(
        AFFINE_TRANSFORMATIONS_VALUES, key, index
    )

    # point = function(point[0], point[1], a, b, c, d, e, f)

    # x = (point[0] + 2.182) * (width - 1) / 4.8378
    # y = (9.9983 - point[1]) * (height - 1) / 9.9983

    x, y = function(x, y, a, b, c, d, e, f)
    scaled_x = (x + 2.182) * (width - 1) / 4.8378
    scaled_y = (9.9983 - y) * (height - 1) / 9.9983
    draw.point((scaled_x, scaled_y), "green")

image.show()


# def generate_stem(x, y):
#     return (0 * x, 0.16 * y)


# def function_2(x, y):
#     return (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6)


# def function_3(x, y):
#     return (0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6)


# def function_4(x, y):
#     return (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44)


# def generate_stem(x, y):
#     return (0 * x + 0 * y + 0), (0 * x + 0.16 * y + 0)


# def generate_successive_ferns(x, y):
#     return (0.85 * x + 0.04 * y + 0), (-0.04 * x + 0.85 * y + 1.6)


# def generate_left_leaves(x, y):
#     return (0.2 * x - 0.26 * y + 0), (0.23 * x + 0.22 * y + 1.6)


# def generate_right_leaves(x, y):
#     return (-0.15 * x + 0.28 * y + 0), (0.26 * x + 0.24 * y + 0.44)
