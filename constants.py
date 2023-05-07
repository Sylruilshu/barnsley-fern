from typing import Callable, Literal


Point = tuple[float, float]
AlgorithmName = Literal[
    "barnsley-fern",
    "alt-barnsley-fern",
    "culcita",
    "cyclosorus",
    "fishbone",
    "fractal-tree",
    "golden-bee",
]
AffineTransformationMapping = dict[int, list[float]]
ScalingFunctionName = Literal[
    "scale_x",
    "scale_y",
]
ScalingFunction = Callable[[float, float], float]
ScalingFunctionMapping = dict[ScalingFunctionName, ScalingFunction]

SCALING_FUNCTION_OPTIONS: dict[AlgorithmName, ScalingFunctionMapping] = {
    "barnsley-fern": {
        "scale_x": lambda x, width: (x + 2.182) * (width - 1) / 4.8378,
        "scale_y": lambda y, height: (9.9983 - y) * (height - 1) / 9.9983,
    },
    "alt-barnsley-fern": {
        "scale_x": lambda x, width: (x + 2.5) * (width - 1) / 5,
        "scale_y": lambda y, height: (8.56 - y) * (height - 1) / 8.7,
    },
    "culcita": {
        "scale_x": lambda x, width: (x + 2) * (width) / 4,
        "scale_y": lambda y, height: (5.8 - y) * (height) / 6,
    },
    "cyclosorus": {
        "scale_x": lambda x, width: (x + 2.5) * (width) / 5,
        "scale_y": lambda y, height: (7.105 - y) * (height) / 7.675,
    },
    "fishbone": {
        "scale_x": lambda x, width: (x + 2.5) * (width) / 5,
        "scale_y": lambda y, height: (7.105 - y) * (height) / 7.675,
    },
    "fractal-tree": {
        "scale_x": lambda x, width: (x + 0.25) * (width) * 2,
        "scale_y": lambda y, height: (0.5 - y) * (height) * 2,
    },
    "golden-bee": {
        "scale_x": lambda x, width: (x + 0.25) * (width) * 2,
        "scale_y": lambda y, height: (0.5 - y) * (height) * 2,
    },
}

ALGORITHM_TRANSFORMATION_OPTIONS: dict[AlgorithmName, AffineTransformationMapping] = {
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

PROBABILITY_OPTIONS: dict[AlgorithmName, list[float]] = {
    "barnsley-fern": [0.01, 0.85, 0.07, 0.07],
    "alt-barnsley-fern": [0.01, 0.85, 0.07, 0.07],
    "culcita": [0.02, 0.84, 0.07, 0.07],
    "cyclosorus": [0.02, 0.84, 0.07, 0.07],
    "fishbone": [0.02, 0.84, 0.07, 0.07],
    "fractal-tree": [0.05, 0.4, 0.4, 0.15],
    "golden-bee": [0.5, 0.5, 0, 0],
}

AFFINE_TRANSFORMATION_INDEXES: list[int] = [1, 2, 3, 4]

STARTING_POINT: tuple[int, int] = (0, 0)
