#input() - A function that prompts the user to enter data
#          Returns the enter data as a string

name = input("What's your name? ")
age = input("How old are you? ")
print(type(age))

#age += 1 
# TypeError: can only concatenate str(not "int") to str
#To solve this error we have to type cast str to int

age = int(age)
print(type(age))
age += 1
print(age)
print(f"Welcome {name}")
print(f"{name}, You're {age} years old")

#Excercise 1: Calculate the Area of a Rectangle
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width
print(f"The Area of {length} and {width} is : {area} cm^2 ")

#Exercise 2: Calculate the Temperature from Fahrenheit to Celcius
f = float(input("Enter the Temperature in(°F): "))
cel = ((f - 32)*5)/9
print(f"Temperature Fahrenheit to Celcius: {cel}")



