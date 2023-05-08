from PIL import Image, ImageDraw
import numpy as np
import click
import os
from constants import (
    ScalingFunctionMapping,
    AlgorithmName,
    AffineTransformationMapping,
    Point,
    STARTING_POINT,
    PROBABILITY_OPTIONS,
    AFFINE_TRANSFORMATION_INDEXES,
    ALGORITHM_TRANSFORMATION_OPTIONS,
    SCALING_FUNCTION_OPTIONS,
)


def transform_point(x: float, y: float, affine_transformation: list[float]) -> Point:
    a, b, c, d, e, f = affine_transformation
    return (a * x + b * y + e), (c * x + d * y + f)


def scale_point(
    x: float,
    y: float,
    width: int,
    height: int,
    scaling_functions: ScalingFunctionMapping,
) -> Point:
    scaled_x = scaling_functions["scale_x"](x, width)
    scaled_y = scaling_functions["scale_y"](y, height)
    return scaled_x, scaled_y


def generate_fractal_point(
    x: float,
    y: float,
    width: int,
    height: int,
    affine_transformation_indexes: list[int],
    probabilities: list[float],
    affine_transformation_mapping: AffineTransformationMapping,
    scaling_function_mapping: ScalingFunctionMapping,
) -> tuple[Point, Point]:
    index = np.random.choice(affine_transformation_indexes, p=probabilities)
    x, y = transform_point(x, y, affine_transformation_mapping[index])
    scaled_x, scaled_y = scale_point(x, y, width, height, scaling_function_mapping)
    return (x, y), (scaled_x, scaled_y)


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
@click.option(
    "--bg-colour",
    "-b",
    default="#000000",
    type=str,
    help="choose background colour using hex",
)
@click.option(
    "--pixel-colour",
    "-pc",
    default="#008000",
    type=str,
    help="choose pixel colour using hex",
)
def main(
    pixels: int,
    iterations: int,
    algorithm_name: AlgorithmName,
    save: bool,
    bg_colour: str,
    pixel_colour: str,
) -> None:
    """
    A utility to generate Barnsley's fern and related fractals.
    """
    width, height = pixels, pixels

    image = Image.new("RGB", (width, height), bg_colour)
    draw = ImageDraw.Draw(image)

    x, y = STARTING_POINT
    for _ in range(iterations):
        points = generate_fractal_point(
            x,
            y,
            width,
            height,
            AFFINE_TRANSFORMATION_INDEXES,
            PROBABILITY_OPTIONS[algorithm_name],
            ALGORITHM_TRANSFORMATION_OPTIONS[algorithm_name],
            SCALING_FUNCTION_OPTIONS[algorithm_name],
        )
        x, y = points[0]
        draw.point(points[1], pixel_colour)

    if save:
        os.makedirs("images", exist_ok=True)
        image.save(f"images/{algorithm_name}.png", quality=95)

    image.show()
    exit(0)


main()
