from random import randint, uniform, random
from tkinter import Tk, Canvas


def generate_random_initial_point() -> tuple[float, float]:
    random_x_coord = round(uniform(-500, 500), 2)
    random_y_coord = round(uniform(-500, 500), 2)
    return (random_x_coord, random_y_coord)


def translate_point(point, affine_transformations, index):
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
# canvas.configure(scrollregion=(-500, -500, 500, -1500))

# for _ in range(100):
#     random_points = []
#     for _ in range(1000):
#         random_point = generate_random_initial_point()
#         random_points.append(random_point)


#     translated_points = []
#     for random_point in random_points:
#         random_num = randint(1, 100)

#         if random_num == 1:
#             index = 1
#         if  1 < random_num <= 86:
#             index = 2
#         if 86 < random_num <= 93:
#             index = 3
#         if 93 < random_num <= 100:
#             index = 4

#         translated_point = translate_point(random_point, affine_transformations, index)
#         translated_points.append(translated_point)

#     for translated_point in translated_points:
#         canvas.create_rectangle(translated_point * 2, outline="green")


random_points = []
for _ in range(10000):
    random_point = generate_random_initial_point()
    random_points.append(random_point)


translated_points = []
# for _ in range(len(random_points)):
one_p = random_points[0:99]
eighty_five = random_points[100:8600]
seven = random_points[8601:9301]
seven_two = random_points[9302:1000]

for point_1 in one_p:
    translated_point = translate_point(point_1, affine_transformations, 1)
    translated_points.append(translated_point)

for point_2 in eighty_five:
    translated_point = translate_point(point_2, affine_transformations, 2)
    translated_points.append(translated_point)

for point_3 in seven:
    translated_point = translate_point(point_3, affine_transformations, 3)
    translated_points.append(translated_point)

for point_4 in seven_two:
    translated_point = translate_point(point_4, affine_transformations, 4)
    translated_points.append(translated_point)


for translated_point in translated_points:
    canvas.create_rectangle(translated_point * 2, outline="green")

root.mainloop()


# for _ in range(100):
#     canvas.create_rectangle(random_point * 2, outline="green")

#     random_num = randint(1, 100)

#     if random_num == 1:
#         index = 1
#     if  1 < random_num <= 86:
#         index = 2
#     if 86 < random_num <= 93:
#         index = 3
#     if 93 < random_num <= 100:
#         index = 4

#     random_point = generate_new_point(random_point, affine_transformations, index)
#     print(random_point)

# root.mainloop()
