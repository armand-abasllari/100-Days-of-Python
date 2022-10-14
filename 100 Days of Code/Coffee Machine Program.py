"""
Coffee Machine Program
"""
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
    }
}
# A dictionary that stores the amount of resources that the coffee machine has.

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Asking the user what they would like to drink.
REPEAT = False
while not REPEAT:
# Asking the user what they would like to drink.
    user_choice =input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "report":
        print(f"Water: {resources['water']} \nMilk: {resources['milk']} \
            \nCoffee: {resources['coffee']}")

    if user_choice == "off":
        break