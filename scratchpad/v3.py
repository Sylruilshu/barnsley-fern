from random import uniform
from tkinter import Tk, Canvas


def test(point):
    x, y = point[0], point[1]
    random_number = uniform(0, 100)
    if random_number < 1:
        return 0, 0.16 * y
    elif 1 <= random_number < 86:
        return 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
    elif 86 <= random_number < 93:
        return 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
    else:
        return -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44


# def test(point):
#     x, y = point[0], point[1]
#     return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6


width = 1000
height = 1000

root = Tk()
root.title("Barnsley's Fern")
canvas = Canvas(root, width=width, height=height, bg="#000000")
canvas.pack()
# canvas.configure(scrollregion=(-500, -500, 500, 500))

# random_point = generate_random_initial_point()
random_point = (1000, 1000)

for _ in range(100000):
    canvas.create_rectangle(random_point * 2, outline="green")
    random_point = test(random_point)
    # print(random_point)


root.mainloop()
