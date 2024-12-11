# Variable:
# A container for a value (string, integer, float, boolean).
# A variable behaves as if it holds the value it contains.

#String - A seiers of Characters 
name = "Anika"
food = "French Fries"
hobby = "Gardening"
email = "xyz@gmail.com"


print(type(name)) #this is a String 
print(f"I am {name}")
print(f"I love {food}")
print(f"I like {hobby}")
print(f"My Email Address is: {email}")
# f-string / F-string:
# It is a special type of string that lets you include variables or expressions 
# inside `{}` for easy and dynamic string creation.



#Integer - a whole number, positive or negative, without decimals, represented by the int data type
age = 20
year = 2024
foodItem = 3

print(type(age))
print(f"I am {age} years old")
print(f"This is {year}")
print(f"I will buy {foodItem} types of rice")


#float - It is a data type used to represent numbers with a decimal point
price = 10.99
print(type(price))
print(f"The price of Banana is {price}")


#complex

x = 1j
print(type(x))


#Boolean - bool is a data type that represents True or False, used for logical operations and decision-making
is_rainy = True
print(is_rainy)


if is_rainy:
    print("It is a rainy weather")
else:
    print("It is a hot weather")
