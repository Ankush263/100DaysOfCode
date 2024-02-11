from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_running = True

while is_running:
    all_items = menu.get_items()
    option = input(f"What would you like? ({all_items}):")

    if option == "off":
        is_running = False
    elif option == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(option)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(
            drink.cost
        ):
            coffee_maker.make_coffee(drink)
