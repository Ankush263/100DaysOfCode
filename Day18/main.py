import random
from turtle import Screen, Turtle, colormode

turtle = Turtle()

colormode(255)


def getRandomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

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

    # movement = 100

    # random_movement = [0, 90, 180, 270]

    # for _ in range(movement):
    #     turtle.speed(10)
    #     turtle.pensize(10)

    #     turtle.forward(30)
    #     turtle.right(random.choice(random_movement))

    #     turtle.color(getRandomColor())


turtle.speed("fastest")


for _ in range(72):
    turtle.circle(80)
    # turtle.forward(10)
    turtle.right(5)
    turtle.color(getRandomColor())

screen = Screen()
screen.exitonclick()
