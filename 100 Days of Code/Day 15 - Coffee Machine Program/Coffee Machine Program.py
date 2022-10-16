"""
Coffee Machine Program
"""
menu = {
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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
resources["Money"] = 0


def deplete_resources(menu_item):
    """
    If the user's choice is in the menu, then deplete the resources needed to make that choice.

    :param menu_item: the name of the menu item the user chose
    """
    if menu_item == "espresso" or menu_item == "latte" or menu_item == "cappuccino":
        for i in ("water", "milk", "coffee"):
            needed = menu[menu_item]["ingredients"].get(i, 0)
            resources[i] -= needed
            if resources[i] < 0:
                print(f"Sorry there is not enough water {i}")


def calculate_resto(menu_item):
    """
    It calculates the resto.
    """
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes  = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    inserted_money = (quarters / 4) + (dimes / 10) + (nickles / 20) + (pennies / 100)

    if menu_item == "espresso" or menu_item == "latte" or menu_item == "cappuccino":
        resto = menu[menu_item]["cost"]
        resources["Money"] += resto
        if inserted_money >= resto:
            return f"Here is ${round(inserted_money - resto,2)} in change.\
            \nHere is your {user_choice} ☕️. Enjoy!"
        if inserted_money <= resto:
            return "Sorry that's not enough money. Money refunded."
        if inserted_money == resto:
            return f"Here is your {user_choice} ☕️. Enjoy!"


SHOULD_CONTINUE = True

while SHOULD_CONTINUE:
    user_choice =input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        SHOULD_CONTINUE = False
    if user_choice == ("espresso") or user_choice == ("latte") or user_choice == ("cappuccino"):
        deplete_resources(user_choice)
        print (calculate_resto(user_choice))
    if user_choice == "report":
        print(f"Water: {resources['water']}\
        \nMilk: {resources['milk']}\
        \nCoffee: {resources['coffee']}\
        \nMoney:${resources['Money']}")
