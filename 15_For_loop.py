# For Loops Demonstration
# Author: [Your Name]
# Description: This script demonstrates various usages of for loops in Python to iterate over ranges, strings, and sequences.

# Loop through a range of numbers from 1 to 10 (inclusive)
# Print each number, followed by a celebratory message
for i in range(1, 11):
    print(i)
print("Happy New Year!")  # Message displayed after the loop ends

# Loop through a range of numbers from 8 to 1 in reverse order
# Print each number, followed by another celebratory message
for i in reversed(range(1, 9)):
    print(i)
print("Happy Holiday!")  # Message displayed after the reverse loop ends

# Loop through a range of numbers from 1 to 10, stepping by 2
# Print each number in the sequence
for i in range(1, 11, 2):
    print(i)

# Iterate through each character in a string (credit card example)
# Print each character separately
credit_card = "1234-5678-9012"
for i in credit_card:
    print(i)

# Loop through a range of numbers from 10 to 29
# Skip printing the number 15 using 'continue'
for i in range(10, 30):
    if i == 15:
        continue  # Skip the current iteration when i is 15
    else:
        print(i)

# Loop through a range of numbers from 10 to 29
# Break the loop completely when i is 25
for i in range(10, 30):
    if i == 25:
        break  # Exit the loop when i is 25
    else:
        print(i)  # Print numbers until the loop exits
