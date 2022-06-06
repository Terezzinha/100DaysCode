# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def generate_report():
    """Shows the amount of ingredients"""
    water_amount = resources["water"]
    milk_amount = resources["milk"]
    coffe_amount = resources["coffee"]
    print(f"Water: {water_amount} \nMilk: {milk_amount} \nCoffe: {coffe_amount}")


# Ask user what he/she like
user_answer = "report"  # input("What would you like? :").lower()
# print(user_answer)

# Report
if user_answer == 'report':
    generate_report()


# TODO: 2. Turn off the coffe machine
# Seguir o caminho
# TODO: 4. Check resources if it is sufficient


def check_is_sufficient(order):
    print(f'--------{order}-----------')

    resources_ammount = resources
    print(f"resources: {resources_ammount} ")

    order_ingredients = MENU[order]
    print(f"Ingredient for {order}: {order_ingredients}")

    print(resources_ammount["water"])
    print(order_ingredients["ingredients"]["water"])
    #print(order_ingredients["ingredients"]["latte"])
    print("\n")

check_is_sufficient('espresso')
check_is_sufficient('latte')
check_is_sufficient('cappuccino')

# TODO: 5. Process Coins

# TODO: 6. Check if the trasaction was sucefful

# TODO: 7. Make Coffe
