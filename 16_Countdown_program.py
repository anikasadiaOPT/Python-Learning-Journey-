"""
Countdown Timer Program
Description:
    A Python program that demonstrates various countdown timer formats.
    The user inputs the countdown time in seconds, and the program displays:
    - A basic countdown.
    - A reversed countdown.
    - A formatted countdown in HH:MM:SS format.
"""

# Importing the required library for adding delays
import time

# Asking the user for the countdown time in seconds
try:
    my_time = int(input("Enter the countdown time in seconds: "))  # User inputs the time
    if my_time <= 0:
        # Validation: If input is non-positive, show an error
        print("Please enter a positive number of seconds for the countdown.")
    else:
        # --- Basic Countdown ---
        print("\nBasic Countdown:")  # Header for the first countdown
        for i in range(0, my_time):  # Loop from 0 to the entered time (exclusive)
            print(i)  # Display the current time step
            time.sleep(2)  # Wait for 2 seconds before continuing to the next step
        print("Time's up!")  # Display message when countdown completes

        # --- Reversed Countdown ---
        print("\nReversed Countdown:")  # Header for the reversed countdown
        for i in reversed(range(0, my_time)):  # Loop from entered time down to 0
            print(i)  # Display the current countdown value
            time.sleep(1)  # Wait for 1 second before the next step
        print("Time Reversed!!")  # Display message when reversed countdown completes

        # --- Formatted Countdown (HH:MM:SS) ---
        print("\nFormatted Countdown (HH:MM:SS):")  # Header for the formatted countdown
        for i in range(my_time, 0, -1):  # Loop from entered time down to 1
            seconds = i % 60  # Extract seconds component (remaining seconds after full minutes)
            minutes = int(i / 60) % 60  # Calculate the minutes component
            hours = int(i / 3600)  # Calculate the hours component
            # Format the time as HH:MM:SS and print it
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)  # Wait for 1 second before the next step
        print("Time Reversed Again!!")  # Display message when formatted countdown completes

# Error handling for invalid input
except ValueError:
    # Display error message if user enters non-numeric input
    print("Invalid input. Please enter a positive integer.")
