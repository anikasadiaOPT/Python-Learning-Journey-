# if-else condition = Executes a block of code if a specified condition is True,
#                     otherwise executes the code block in the else statement.


# Example 1: Book purchase decision based on price
price = float(input("Enter the price of books: "))
if price < 100 and price > 0:
    print("I will buy them")
elif price >= 100 and price < 1000:
    print("I need discount")
else:
    print("I won't buy them")




# Example 2: Movie ticket discount decision
# Prompt for a response to buy a movie ticket
response = input("Would you like to buy a Movie Ticket (Y/N):").strip().upper() # .strip(): Removes any leading or trailing whitespace.
                                                                                 # .upper(): Converts the string to uppercase.
if response == "Y":
   print("You will get a discount") # If user responds with 'Y' or y, they get a discount
elif response == "N":
   print("You won't get a discount") # If user responds with 'N' or n, they will not get a discount
else:
   print("Invalid input . Please enter only Y or N")
   
   
   
# Example 3: Eligibility for open credit based on completed credits
course_selection = int(input("Enter the total credit you have completed: "))
if course_selection >= 15:
   print("You are eligible for open credit")  # Eligible for open credit with 15 or more credits
elif course_selection <15 and course_selection > 0:
   print("You are not eligible for open credit")  # Not eligible for open credit with less than 15 and positive credits
else:
   print("Enter a valid number")              # Handle zero or negative credits 
   

#Exercise 4: Calculate the Temperature from Fahrenheit to Celcius
#            & Celcius to Fahrenheit
unit = input("Enter the unit in(F/C): ").strip().upper()
temp = float(input("Enter the Temperature: "))
if unit == "C":
    F = round((9 * temp) / 5 + 32, 2)
    print(f"Temperature Celcius to Fahrenheit: {F}°F")
elif unit == "F":
    C = round(((temp - 32)*5)/9,2)
    print(f"Temperature Fahrenheit to Celcius: {C}°C")
else:
    print("Invalid")

