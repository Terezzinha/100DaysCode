
# Calculator
from art import logo


def add(n1, n2):
    return n1 + n2


def subtrac(n1, n2):
    """Subtrac n2 (number) from n1 (number) """
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Nao pode dividir por zero"
    return n1/n2


operations = {
    "+": add,
    "-": subtrac,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What's is the first  number?:"))
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Choose operation:")
        num2 = float(input("What's is the next number?:"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type y to contininue calculating with {answer}: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
