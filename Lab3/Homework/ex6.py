from turtle import *
from ex5 import draw_star
# def draw_star(x, y, length):
# #     penup()
# #     goto(x, y)
# #     pendown()
# #     left(36)
# #     for i in range(5):
# #         forward(length)
#         left(144)
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

