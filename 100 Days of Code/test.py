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



should_continue = True

while should_continue:
    user_choice =input("What would you like? (espresso/latte/cappuccino): ")


    def deplete_resources(menu_item):
        """
        If the user's choice is in the menu, then deplete the resources needed to make that choice.

        :param menu_item: the name of the menu item the user chose
        """
        if menu_item == "espresso" or menu_item == "latte" or menu_item == "cappuccino":
            for i in ("water", "milk", "coffee"):
                needed = menu[menu_item]["ingredients"].get(i, 0)
                resources[i] -= needed
        elif menu_item == "report":
            print(f"Water: {resources['water']}\
            \nMilk: {resources['milk']}\
            \nCoffee: {resources['coffee']}")


    deplete_resources(menu_item=user_choice)
