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
    print(f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffe: {resources['coffee']} \nProfit: R$ {machine_profit}")


def check_is_sufficient(order_ingredients):
    """Check if there are sufficient supplies to make the order"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, the is not enough {item}")


machine_is_on = True
machine_profit = 0

while machine_is_on:
    # Ask user what he/she like
    user_choice = input("What would you like? (e/l/c): ").lower()
    if user_choice == "off":
        machine_is_on = False

    # machine is ON
    elif user_choice == 'report':
        generate_report()

        # TODO: 2. Turn off the coffe machine
        # Seguir o caminho
        # TODO: 4. Check resources if it is sufficient
    else:
        drink_order = MENU[user_choice]
        print(f"drink_order: {drink_order}")
        check_is_sufficient(drink_order['ingredients'])

        # TODO: 5. Process Coins

        # TODO: 6. Check if the trasaction was sucefful

        # TODO: 7. Make Coffe
