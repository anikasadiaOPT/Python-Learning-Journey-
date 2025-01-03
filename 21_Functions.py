# Function = A block of reusable code 
#           place() after the function name to invoke  it 

name = input("Name: ")
age = int(input("Age: "))

def welcome(name, age):    
    print(f"Welcome {name}")
    print(f"You are {age} years old")
    print("Have a nice a day!")
    print("You can visit the whole city")
    
welcome(name,age)
name = input("Name: ")
age = int(input("Age: "))
welcome(name, age)
name = input("Name: ")
age = int(input("Age: "))
welcome(name, age)

print()
username = input("Enter username: ")
amount = float(input("Amount: "))
dueDate = input("dueDate: ")
def displayInvoice(username, amount, dueDate):
    print(f"Your username is: {username}")
    print(f"Your bill of ${amount:.2f} is due: {dueDate}")
    
    
displayInvoice(username, amount, dueDate)


# return statement = is used to end a function
#                    and send a result back to the caller
x = int(input("Enter X: "))
y = int(input("Enter y: "))

def addition(x, y):
    return x+y
def substraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y 
def modulus(x,y):
    return x%y
def exponent(x,y):
    return pow(x,y)
    
print(addition(x,y))
print(substraction(x,y))
print(multiplication(x,y))
print(division(x,y))
print(modulus(x,y))
print(exponent(x,y))
