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
    """Check if there are sufficient supplies to make the order
    Return True ou False
    """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, the is not enough {item}")
            return False
    return True


def process_coins():
    """"Return the total calculated from coins inserted
    Quarter = $0.25 - Dimes = $0.10 - Nickles = $0.05 - Pennies = $0.01 
    """
    print("Please, insert do coins: ")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))

    total = 0
    if quarters > 0:
        total += quarters * 0.25
    if dimes > 0:
        total += dimes * 0.10
    if nickles > 0:
        total += nickles * 0.05
    if pennies > 0:
        total += pennies * 0.05

    return total


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

    else:
        drink_order = MENU[user_choice]
        print(f"drink_order: {drink_order}")
        if check_is_sufficient(drink_order['ingredients']):
            print(f"Total: $ {process_coins()}")
            
            # TODO: 5. Process Coins
            # TODO: 6. Check if the trasaction was sucefful
            # TODO: 7. Make Coffe
