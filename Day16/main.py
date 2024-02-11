# from turtle import Screen, Turtle

from prettytable import PrettyTable

# timmy = Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(250)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()

table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmender"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align["Pokemon name"] = "l"
table.align["Type"] = "l"
print(table)
