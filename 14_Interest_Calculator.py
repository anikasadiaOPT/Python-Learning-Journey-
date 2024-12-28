# Python Compound Interest Calculator

# What is Interest? 
# Interest is the monetary charge for the privilege of borrowing money. It is the cost paid by borrowers for 
# borrowing money, often expressed as an annual percentage rate (APR). 
# Interest can also refer to the ownership percentage that a stockholder has in a company.

# This program calculates the compound interest and determines the final amount after a specified time period.

# Initialize variables
final_amount = 0  # To store the calculated final amount
principal = 0  # The principal amount
rate = 0  # The annual interest rate
time_period = 0  # The time period in years

# Get valid principal amount
while True:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Error: Principal amount can't be less than or equal to zero.")
    else:
        break

# Get valid rate of interest
while True:
    rate = float(input("Enter the annual interest rate (in percentage): "))
    if rate <= 0:
        print("Error: Interest rate can't be less than or equal to zero.")
    else:
        break

# Get valid time period
while True:
    time_period = int(input("Enter the time period (in years): "))
    if time_period <= 0:
        print("Error: Time period can't be less than or equal to zero.")
    else:
        break

# Calculate compound interest
final_amount = principal * pow((1 + rate / 100), time_period)

# Display the results
print(f"The Final Amount after {time_period} year(s): ${final_amount:.3f}")
