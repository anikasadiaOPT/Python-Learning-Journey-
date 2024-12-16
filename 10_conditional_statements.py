# Conditional Expressions in Python (Ternary Operator)
# A conditional expression provides a one-line shortcut for the if-else statement.
# Syntax: X if condition else Y

# Example 1: Determine if a number is positive or negative
num = 5
print("Positive" if num > 0 else "Negative")  # Check if the number is positive or negative

# Example 2: Check if a number is EVEN or ODD
result = "EVEN" if num % 2 == 0 else "ODD"  # Conditional expression based on remainder
print(result)

# Example 3: Find the maximum of two numbers
a = 4
b = 7
max_num = a if a > b else b  # Returns the larger of 'a' and 'b'
print(max_num)

# Example 4: Find the minimum of two numbers
min_num = a if a < b else b  # Returns the smaller of 'a' and 'b'
print(min_num)

# Example 5: Check voting eligibility based on age
age = 20
eligibility = "Eligible for vote" if age >= 18 else "Not eligible"  # Voting eligibility check
print(eligibility)

# Example 6: Check if the temperature is warm or cold
temp = 30
checking = "Warm" if temp > 20 else "Cold"  # Temperature condition based on a threshold of 20°C
print(checking)

# Example 7: Determine access level for a user
user_access = "ADMIN"
access = "Full access" if user_access == "ADMIN" else "Limited Access"  # Assign access level based on user type
print(access)
