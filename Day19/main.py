from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_up():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_down():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(move_forwards, "d")
screen.onkey(move_backwards, "a")
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(clear, "c")

screen.listen()
screen.exitonclick()
