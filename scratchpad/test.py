from random import randint, uniform, random
from tkinter import Tk, Canvas


def generate_random_initial_point() -> tuple[float, float]:
    random_x_coord = round(uniform(-500, 500), 2)
    random_y_coord = round(uniform(-500, 500), 2)
    return (random_x_coord, random_y_coord)


def generate_new_point(point, affine_transformations, index):
    a = affine_transformations[index][0]
    b = affine_transformations[index][1]
    c = affine_transformations[index][2]
    d = affine_transformations[index][3]
    f = affine_transformations[index][4]

    x = point[0]
    y = point[1]

    return (a * x + b * y, c * x + d * y + f)


affine_transformations = {
    1: [0, 0, 0, 0.16, 0],
    2: [0.85, 0.04, -0.04, 0.85, 1.6],
    3: [0.2, -0.26, 0.23, 0.22, 1.6],
    4: [-0.15, 0.28, 0.26, 0.24, 0.44],
}


width = 1000
height = 1000

root = Tk()
root.title("Barnsley's Fern")
canvas = Canvas(root, width=width, height=height, bg="#000000")
canvas.pack()
canvas.configure(scrollregion=(-500, -500, 500, 500))
canvas.xview_moveto(0.5)
canvas.yview_moveto(0.5)


canvas.create_rectangle(random_point * 2, outline="green")

root.mainloop()
