from random import uniform, random
from tkinter import Tk, Canvas
import numpy as np


def function_1(point: tuple[float, float]):
    first = np.array([[0, 0], [0, 0.16]])
    second = np.array([[point[0]], [point[1]]])
    final = first.dot(second)
    return (final[0][0], final[1][0])


def function_2(point: tuple[float, float]):
    first = np.array([[0.85, 0.04], [-0.04, 0.85]])
    second = np.array([[point[0]], [point[1]]])
    third = np.array([[0], [1.6]])

    final = first.dot(second)
    final = final + third
    return (final[0][0], final[1][0])


def function_3(point: tuple[float, float]):
    first = np.array([[0.2, -0.26], [0.23, 0.22]])
    second = np.array([[point[0]], [point[1]]])
    third = np.array([[0], [1.6]])

    final = first.dot(second)
    final = final + third
    return (final[0][0], final[1][0])


def function_4(point: tuple[float, float]):
    first = np.array([[-0.15, 0.28], [0.26, 0.24]])
    second = np.array([[point[0]], [point[1]]])
    third = np.array([[0], [0.44]])

    final = first.dot(second)
    final = final + third
    return (final[0][0], final[1][0])


def generate_random_initial_point() -> tuple[float, float]:
    random_x_coord = round(uniform(-500, 500), 2)
    random_y_coord = round(uniform(-500, 500), 2)
    return (random_x_coord, random_y_coord)


width = 1000
height = 1000

root = Tk()
root.title("Barnsley's Fern")
canvas = Canvas(root, width=width, height=height, bg="#000000")
canvas.pack()
canvas.configure(scrollregion=(-500, -500, 500, 500))

# random_point = generate_random_initial_point()
random_point = (0, 0)

for _ in range(1000):
    canvas.create_rectangle(random_point * 2, outline="green")

    if 0 <= random() < 0.01:
        translated_point = function_1(random_point)
        random_point = translated_point
        continue
    if 0.01 < random() <= 0.86:
        translated_point = function_2(random_point)
        random_point = translated_point
        continue
    if 0.86 < random() <= 0.93:
        translated_point = function_3(random_point)
        random_point = translated_point
        continue
    if 0.93 < random() <= 1:
        translated_point = function_4(random_point)
        random_point = translated_point
        continue

root.mainloop()
