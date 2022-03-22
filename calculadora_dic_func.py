
#Calculator
def add(n1,n2):
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
"/":divide
}

num1 = int(input("What's is the first  number?:"))
for symbol in operations:
  print(symbol)

should_continue = ca  
operation_symbol = input("Choose operator:")
num2 = int(input("What's is the second  number?:"))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

operation_symbol = input("Pick another operation: ")
num3 = int (input("what's the next number? :"))
calculation_function = operations[operation_symbol]
answer = calculation_function (calculation_function(num1,num2),num3)

