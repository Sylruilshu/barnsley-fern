from PIL.Image import Image as image
from PIL import Image, ImageDraw
import numpy as np
import click
import os
from constants import (
    ScalingFunctionMapping,
    AlgorithmName,
    AffineTransformationMapping,
    X,
    Y,
    PROBABILITY_OPTIONS,
    AFFINE_TRANSFORMATION_INDEXES,
    ALGORITHM_TRANSFORMATION_OPTIONS,
    SCALING_FUNCTION_OPTIONS,
)


def transform_point(
    x: float, y: float, affine_transformation: list[float]
) -> tuple[float, float]:
    a, b, c, d, e, f = affine_transformation
    return (a * x + b * y + e), (c * x + d * y + f)


def scale_point(
    x: float,
    y: float,
    width: int,
    height: int,
    scaling_functions: ScalingFunctionMapping,
) -> tuple[float, float]:
    scaled_x = scaling_functions["scale_x"](x, width)
    scaled_y = scaling_functions["scale_y"](y, height)
    return scaled_x, scaled_y


def generate_fractal(
    x: float,
    y: float,
    width: int,
    height: int,
    iterations: int,
    probabilities: list[float],
    affine_transformation_mapping: AffineTransformationMapping,
    scaling_function_mapping: ScalingFunctionMapping,
) -> image:
    image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(image)

    for _ in range(iterations):
        index = np.random.choice(AFFINE_TRANSFORMATION_INDEXES, p=probabilities)
        x, y = transform_point(x, y, affine_transformation_mapping[index])
        scaled_x, scaled_y = scale_point(x, y, width, height, scaling_function_mapping)
        draw.point((scaled_x, scaled_y), "green")

    return image


@click.command()
@click.option("--pixels", "-p", default=1000, type=int, help="Set window size")
@click.option(
    "--iterations", "-i", default=100000, type=int, help="Amount of points to generate"
)
@click.option(
    "--algorithm-name",
    "-a",
    default="barnsley-fern",
    type=click.Choice(list(ALGORITHM_TRANSFORMATION_OPTIONS.keys())),
    help="The fractal to generate",
)
@click.option(
    "--save/--no-save",
    "-s/-n",
    default=False,
    type=bool,
    help="Save generated image to ./images/{algorithm_name}.png",
)
def main(
    pixels: int, iterations: int, algorithm_name: AlgorithmName, save: bool
) -> None:
    """
    A utility to generate Barnsley's fern and related fractals.
    """
    width, height = pixels, pixels

    image = generate_fractal(
        X,
        Y,
        width,
        height,
        iterations,
        PROBABILITY_OPTIONS[algorithm_name],
        ALGORITHM_TRANSFORMATION_OPTIONS[algorithm_name],
        SCALING_FUNCTION_OPTIONS[algorithm_name],
    )

    if save:
        os.makedirs("images", exist_ok=True)
        image.save(f"images/{algorithm_name}.png", quality=95)

    image.show()

    exit(0)


main()


# pixels = 5000
# iterations = 10000000
