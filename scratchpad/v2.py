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
    e = affine_transformations[index][4]
    f = affine_transformations[index][5]

    x = point[0]
    y = point[1]

    return (a * x + b * y + e, c * x + d * y + f)


affine_transformations = {
    1: [0, 0, 0, 0.16, 0, 0],
    2: [0.85, 0.04, -0.04, 0.85, 0, 1.6],
    3: [0.2, -0.26, 0.23, 0.22, 0, 1.6],
    4: [-0.15, 0.28, 0.26, 0.24, 0, 0.44],
}


width = 1000
height = 1000

root = Tk()
root.title("Barnsley's Fern")
canvas = Canvas(root, width=width, height=height, bg="#000000")
canvas.pack()
canvas.configure(scrollregion=(-500, -500, 500, 500))
# canvas.configure(scrollregion=(-500, -500, 500, -1500))

# random_point = generate_random_initial_point()
random_point = (0, 0)

for _ in range(100):

    random_num = randint(1, 100)

    # if random_num == 1:
    #     index = 1
    # if 2 <= random_num <= 85:
    #     index = 2
    # if 86 < random_num <= 93:
    #     index = 3
    # if 93 < random_num <= 100:
    #     index = 4

    if random() < 0.1:
        index = 1
        print("1")
    if 0.1 < random() <= 0.6:
        index = 2
        print("85")
    if 0.6 < random() <= 0.76:
        index = 3
        print("7")
    if 0.76 < random() <= 1:
        index = 4
        print("7-2")

    random_point = generate_new_point(random_point, affine_transformations, index)
    canvas.create_rectangle(random_point * 2, outline="green")
    print(random_point)

root.mainloop()
