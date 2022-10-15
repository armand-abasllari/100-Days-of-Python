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

user_choice =input("What would you like? (espresso/latte/cappuccino): ")


def return_report():
    """
    If the user chooses "report", the function returns a string
    with the current amount of water, milk,and coffee.
    """
    return f"Water: {resources['water']} \nMilk: {resources['milk']} \
                \nCoffee: {resources['coffee']}"

return_report()

def return_resources(menu_item):

    for menu_item in ("espresso", "latte", "cappuccino"):
        if user_choice == "espresso":
            resources['water'] -= menu['espresso']['ingredients']['water']
            resources['coffee'] -= menu['espresso']['ingredients']['coffee']
            break
        elif user_choice == "latte":
            resources['water'] -= menu['latte']['ingredients']['water']
            resources['coffee'] -= menu['latte']['ingredients']['coffee']
            resources['milk'] -= menu['latte']['ingredients']['milk']
            break
        elif user_choice == "cappuccino":
            resources['water'] -= menu['cappuccino']['ingredients']['water']
            resources['coffee'] -= menu['cappuccino']['ingredients']['coffee']
            resources['milk'] -= menu['cappuccino']['ingredients']['milk']
            break
return_resources(menu_item=user_choice)

print(resources)
