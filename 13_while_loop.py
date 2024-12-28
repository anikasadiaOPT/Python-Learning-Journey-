# A simple program demonstrating the use of while loops in Python
# The program interacts with the user to collect and process input

# Prompt the user to enter their hobby
# Keep asking until a valid input is provided
hobby = input("Enter your hobby: ")

while hobby == "":
    print("You did not enter your hobby.")  # Notify the user about invalid input
    hobby = input("Enter your hobby: ")

print(f"Amazing hobby: {hobby}")

# Prompt the user to enter their favorite dish
# Continue until the user decides to quit by entering 'q'
fvrt_dish = input("Enter your favorite dish (q to quit): ")

while fvrt_dish != "q":
    print(f"You like {fvrt_dish}")  # Acknowledge the input
    fvrt_dish = input("Enter your favorite dish (q to quit): ")

print("Bye Bye")

# Prompt the user to enter a number within a specific range (0 to 10)
# Keep asking until a valid input is provided
num = int(input("Enter a number between 0 and 10: "))

while num < 0 or num > 10:
    print(f"Your entered {num}. Please enter a valid number.")  # Inform the user about invalid input
    num = int(input("Enter a number between 0 and 10: "))

print(f"Your number is {num}")

# End of the program
