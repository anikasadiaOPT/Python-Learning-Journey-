#Type casting - The process of converting a variable from one data type to another
#               str(), int(), float(), bool()
# It is mostly efficient while handling user input because user input's are always a String

name = "Anika"
age = 20
gpa = 3.78
isStudent = True;


# int to float 
age = float(age)
print(age)
print(type(age))


#float to int
gpa = int(gpa)
print(gpa)
print(type(gpa))


#bool to string
isStudent = str(isStudent)
print(isStudent)
print(type(isStudent))


#string to bool
name = bool(name)
print(name) # True - because it has some value in it
print(type(name)) 

city = ""
city = bool(city)
print(city) # False - because it has empty value in it


#string to int

#name = int(name)
#print(name)

#Value error - invalid literals for int() with base 10: 'Anika'
#This error occurs while trying to convert a non-numeric string like 'Anika' into an integer using int(), 
#which only works for valid numeric strings. For example-

price = "3550"
print(type(price)) # <class 'str'>
price = int(price)
print(price)
print(type(price)) # <class 'int'>



