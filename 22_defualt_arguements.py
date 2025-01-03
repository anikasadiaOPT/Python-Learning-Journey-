# Default Arguments and Countdown Program

# --- Default Arguments Demonstration ---
# Function: netPrice
# This function calculates the net price after applying a discount and tax.
# Parameters:
#     listPrice (float): The original price of the item.
#     discount (float): The discount percentage in decimal form (default: 0).
#     tax (float): The tax percentage in decimal form (default: 0.05).
# Returns:
#     float: The final price after applying the discount and tax.

def netPrice(listPrice, discount=0, tax=0.05):
    """
    Calculate the net price after discount and tax.
    
    Args:
        listPrice (float): Original price of the item.
        discount (float): Discount rate as a decimal (default: 0).
        tax (float): Tax rate as a decimal (default: 0.05).

    Returns:
        float: Final net price.
    """
    return listPrice * (1 - discount) * (1 + tax)

# Example Usage
original_price = 500  # Original price of the product
applied_discount = 0.01  # 1% discount
tax_rate = 0.05  # Default tax rate (5%)

final_price = netPrice(original_price, applied_discount)
print(f"The net price of the item is: ${final_price:.2f}")

# --- Countdown Program ---
# Function: count
# This function performs a countdown from a given start to end value with a delay between each number.
# Parameters:
#     start (int): The starting value of the countdown.
#     end (int): The ending value of the countdown.
# Prints:
#     The countdown sequence followed by "DONE!".

import time  # Required to implement delay in countdown

def count(start, end):
    """
    Perform a countdown from the start value to the end value with a 1-second interval.

    Args:
        start (int): The starting number of the countdown.
        end (int): The ending number of the countdown.
    """
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)  # Delay of 1 second between counts
    print("DONE!")

# Example Usage
print("Starting Countdown:")
count(0, 10)
