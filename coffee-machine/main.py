MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}


def add_money(money):
    print("Please insert coins\n")
    total = 0
    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01,
    }

    for coin in coins:
        m = int(input(f"how many {coin}?: "))
        total += round(m * coins[coin], 2)

    money = total
    return money


def check_and_service(money, option):
    if MENU[option]["cost"] > money:
        return False
    else:
        return True


def make_coffee():
    total_items = {"Water": 300, "Milk": 200, "Coffee": 100}
    total_money = 0
    served_finish = False

    while not served_finish:
        option = input("What would you like (espresso/latte/cappuccino): ")

        if option == "report":
            print(
                f"Water: {total_items['Water']}ml \nMilk: {total_items['Milk']}ml \nCoffee: {total_items['Coffee']}g \nMoney: ${total_money}"
            )
        elif option == "off":
            served_finish = True
        else:
            money = add_money(total_money)
            service_success = check_and_service(money, option)
            if not service_success:
                print("Sorry that's not enough money. Money refunded.")
            else:
                total_items["Coffee"] -= MENU[option]["ingredients"]["coffee"]
                total_items["Milk"] -= MENU[option]["ingredients"]["milk"]
                total_items["Water"] -= MENU[option]["ingredients"]["water"]

                if total_items["Coffee"] <= 0:
                    return print("Sorry there is not enough coffee.")
                elif total_items["Water"] <= 0:
                    return print("Sorry there is not enough water.")
                elif total_items["Milk"] <= 0:
                    return print("Sorry there is not enough milk.")

                total_money += money
                print(f"Here is your {option}. Enjoy!")


make_coffee()
