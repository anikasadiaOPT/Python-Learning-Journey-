# Python Calculator
import math
num1 = float(input("Enter the 1st number: "))
op = input("Enter an operator(+,-,**,/,%,//, sqrt, log, sin, cos,tan, !): ")

if op in ["+","-","*","**","/","%","//"]:
    num2 = float(input("Enter the 2nd number: "))

# Basic arithmetic operations
if op == "+":
   result = num1 + num2
   print(round(result))
   
elif op == "-":
   result = num1 - num2
   print(round(result))
   
elif op == "*":
   result = num1 * num2
   print(round(result))
   
elif op == "**":
   result = num1 ** num2
   print(round(result,2))

elif op == "/":
   result = num1 / num2
   print(round(result,2))
   
elif op == "%":
   result = num1 % num2
   print(round(result))
   
elif op == "//":
   result = num1 // num2
   print(round(result))
   
# Square root operation
elif op == "sqrt":
   if num1 >= 0:
      result = round(math.sqrt(num1), 3)
      print(f"Square root of {num1} is: {result}")
   else:
        print("Cannot compute the square root")
      
# Logarithmic operations
elif op == "log":
    log_type = input("Enter 'natural' for natural log or 'base10' for base-10 log: ").strip().lower()
    if log_type == "natural":
       result = round(math.log(num1), 3)
       print(f"Natural log: {result}")
    elif log_type == "base10":
       result = round(math.log10(num1),3)
       print(f"Base-10 log: {result}")
    else:
        print("Invalid log type.")

# Trigonometric operations
elif op == "sin":
    print(f"Sine: {round(math.sin(math.radians(num1)),3)}")
elif op == "cos":
    print(f"Cosine: {round(math.cos(math.radians(num1)), 3)}")
elif op == "tan":
    print(f"Tangent: {round(math.tan(math.radians(num1)), 3)}")
    
# Factorial operation
elif op == "!":
    if num1.is_integer() and num1 >= 0:
        result = math.factorial(int(num1))
        print(f"Factorial: {result}")
    else:
        print("Factorial is not defined for negative numbers or non-integers.")

else:
   print(f"{op} is not a valid operator")

 
