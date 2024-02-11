import random
from turtle import Screen, Turtle, colormode

turtle = Turtle()

colormode(225)


def getRandomColor():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)

    return (r, g, b)


# def rotate_times(times):
#     temp = times
#     while times != 0:
#         turtle.forward(100)
#         turtle.right(360 / temp)
#         times -= 1


# time = 3
# while time < 10:
#     rotate_times(time)
#     time += 1

movement = 100

random_movement = [0, 90, 180, 270]

for _ in range(movement):
    turtle.speed(10)
    turtle.pensize(10)

    turtle.forward(30)
    turtle.right(random.choice(random_movement))

    turtle.color(getRandomColor())


screen = Screen()
screen.exitonclick()
