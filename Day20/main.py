import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

segments = []
x_axis = 0
for _ in range(3):
    t = Turtle("square")
    t.color("white")
    t.penup()
    t.setpos(x_axis, 0)
    x_axis -= 20
    segments.append(t)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].right(90)


screen.exitonclick()
