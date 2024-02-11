import random
from turtle import Screen, Turtle

screen = Screen()

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    "Make your bet", "Which turtle will win the race? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []

y_axis = -100

for color in colors:
    t = Turtle("turtle")
    t.color(color)
    t.penup()
    t.goto(-230, y_axis)
    y_axis += 40
    all_turtle.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You have won! the {winning_color} turtle is the winner!")
            else:
                print("You lose")

            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
