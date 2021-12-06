
























#calculator

#add
def add(n1, n2):
  return n1 + n2

#subtract 
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("What's the first number?: "))
for key in operations:
  print(key)
operation_symbol = input("Pick a operation from the line above: ")
num2 = int(input("What's the second number?: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick a operation from the line above: ")
num3 = int(input("What's the second number?: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(calculation_function(num1, num2), num3)
print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")