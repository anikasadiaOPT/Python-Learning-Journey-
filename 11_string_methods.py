import string
import random

# Program for various user input operations

# Hobby-related operations
hobby = input("Enter your hobby: ")
# Length of the hobby string
hobby_length = len(hobby)
print(f"Length of your hobby: {hobby_length}")

# Finding the first occurrence of "o"
hobby_o_position = hobby.find("o")
print(f"First occurrence of 'o': {hobby_o_position if hobby_o_position != -1 else 'Not found'}")

# Finding the last occurrence of "q"
hobby_q_position = hobby.rfind("q")
print(f"Last occurrence of 'q': {hobby_q_position if hobby_q_position != -1 else 'Not found'}")

# Capitalizing the hobby
hobby_capitalized = hobby.capitalize()
print(f"Hobby capitalized: {hobby_capitalized}")

# Name-related operations
name = input("Enter your name: ")
# Convert name to uppercase
name_upper = name.upper()
print(f"Name in uppercase: {name_upper}")
# Convert name to lowercase
name_lower = name.lower()
print(f"Name in lowercase: {name_lower}")
# Check if the name is a digit
name_isdigit = name.isdigit()
print(f"Is the name a digit? {name_isdigit}")
# Check if the name contains only alphabetic characters
name_isalpha = name.isalpha()
print(f"Does the name contain only alphabetic characters? {name_isalpha}")

# Phone number-related operations
phone_number = input("Enter your phone number: ")
# Replacing dashes with commas
phone_number_replaced = phone_number.replace("-", ",")
print(f"Phone number with dashes replaced by commas: {phone_number_replaced}")

# Username validation exercise
# Validate username with specific criteria:
# - Must be no more than 12 characters
# - Cannot contain spaces
# - Must contain alphabetic characters and special characters

username = input("Enter a username: ")
if len(username) > 12:
    print("Error: Username cannot be more than 12 characters.")
elif " " in username:
    print("Error: Username cannot contain spaces.")
elif not username.isalpha():
    print("Error: Username can only contain alphabetic characters.")
else:
    print(f"Welcome, {username}!")

# Additional functions can be added for other user validations if needed.

# Password Validation Program
password = input("Enter your password: ")

# Validation flags
is_valid_length = len(password) >= 8                                          # Rule 1: Minimum 8 characters
has_uppercase = any(char.isupper() for char in password)                      # Rule 2: At least one uppercase letter
has_lowercase = any(char.islower() for char in password)                      # Rule 2: At least one lowercase letter
has_digit = any(char.isdigit() for char in password)                          # Rule 3: At least one digit
special_characters = string.punctuation                                       # Contains all special characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
has_special_character = any(char in special_characters for char in password)  # Rule 4: At least one special character
no_spaces = " " not in password                                               # Rule 5: No spaces

# Check all conditions
if is_valid_length and has_uppercase and has_digit and no_spaces:
    print("Password is valid.")
else:
    print("Password is invalid. Please follow the rules:")
    if not is_valid_length:
        print("- Password must be at least 8 characters long.")
    if not has_uppercase:
        print("- Password must contain at least one uppercase letter.")
    if not has_lowercase:
        print("- Password must contain at least one lowercase letter.")
    if not has_digit:
        print("- Password must contain at least one digit.")
    if not has_special_character:
        print("- Password must contains at least one special character.")
    if not no_spaces:
        print("- Password must not contain spaces.")

