import art
print(art.logo1)

def add(n1, n2):
  """Adds n1 and n2 numbers and 
  returns the sum"""
  return n1+n2
  
def sub(n1, n2):
  """subtract n1 and n2 and returns the difference"""
  return n1-n2

def mul(n1, n2):
  """Multiply n1 and n2 and returns the product of 2 numbers"""
  return n1*n2

def div(n1, n2):
  """Divides n1 and n2 and provides the result"""
  return n1/n2

n1 = float(input("what's the first number: "))
operator = input("Enter an operator: + - * /: \n")
n2 = float(input("what's the second number: "))

continue_calc = True

while continue_calc:
  def calc(n1, operator, n2):
    """Calculates numbers based on operaton"""
    if operator == "+":
      return add(n1, n2)
    elif operator == "-":
      return sub(n1, n2)
    elif operator == "*":
      return mul(n1, n2)
    elif operator == "/":
      return div(n1, n2)
  answer = calc(n1, operator, n2)
  print(f"Result: {n1} {operator} {n2} = {answer}")

  cont = input("Type 'y' to continue calculating with or type 'n' to start new calculation: ")
  if cont == "y":
    n1 = answer
    operator = input("Enter an operator: + - * /: \n")
    n2 = float(input("Enter another number n2: "))
    calc(n1, operator, n2)
  else:
    n1 = float(input("Enter a number n1: "))
    operator = input("Enter an operator: + - * /: \n")
    n2 = float(input("Enter another number n2: "))
    calc(n1, operator, n2)

# ------------------------------ Option 2 ----------------------------------------------
# import art

# def add(n1, n2):
#   """Adds n1 and n2 numbers and 
#   returns the sum"""
#   return n1+n2

# def sub(n1, n2):
#   """subtract n1 and n2 and returns the difference"""
#   return n1-n2

# def mul(n1, n2):
#   """Multiply n1 and n2 and returns the product of 2 numbers"""
#   return n1*n2

# def div(n1, n2):
#   """Divides n1 and n2 and provides the result"""
#   return n1/n2

# oper = {
#   "+" : add,
#   "-" : sub,
#   "*" : mul,
#   "/" : div
# }

# def calculator(): 
#   print(art.logo1)
#   n1 = float(input("what's the first number: "))
#   for key in oper:
#     print(key) 
  
#   continue_cal = True
  
#   while continue_cal:
#     operation_symbol = input("Pick an operation: ")
#     n2 = float(input("what's the next number: "))
#     calculation = oper[operation_symbol]
#     answer = calculation(n1, n2)
    
#     print(f"Result: {n1} {operation_symbol} {n2} = {answer}")
    
#     cont = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation: ")
#     if cont == "y":
#       n1 = answer
#     else:
#       continue_cal = False
#       calculator()

# calculator()