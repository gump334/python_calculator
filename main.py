
























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

def calculator():
  num1 = int(input("What is the first number?: "))
  while True:
    for key in operations:
      print(key)
    operation_symbol = input("Pick a operation from the line above: ")
    num2 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    keep_calculating = input("do you want to continue calculating? yes no=restart or any key=end: ").lower()
    if keep_calculating == "yes":
      num1 = answer
      continue   
    elif keep_calculating == "no":
      calculator()
    else:
      print("Thank you for using a calculator created by Terrell from Black Cloud Geeks ")
      break
calculator()