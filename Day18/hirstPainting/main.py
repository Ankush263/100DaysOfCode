import random
from turtle import Screen, Turtle, colormode

turtle = Turtle()
colormode(255)

color_list = [
    (220, 152, 56),
    (108, 168, 226),
    (245, 207, 46),
    (195, 44, 101),
    (169, 178, 12),
    (91, 15, 63),
    (18, 85, 208),
    (165, 2, 25),
    (211, 58, 30),
    (3, 53, 159),
    (208, 96, 154),
    (57, 124, 98),
    (54, 37, 36),
    (77, 70, 191),
    (51, 38, 66),
    (197, 130, 162),
]

turtle.penup()
x = -300
y = -300
turtle.setposition(x, y)
turtle.pendown()
turtle.speed("fastest")

outer_count = 10
while outer_count > 0:
    inner_count = 10
    while inner_count > 0:
        turtle.dot(20, random.choice(color_list))
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        inner_count -= 1

    turtle.penup()
    temp_y = y + 50
    y = temp_y
    turtle.setposition(x, temp_y)
    turtle.pendown()
    outer_count -= 1

screen = Screen()
screen.exitonclick()
