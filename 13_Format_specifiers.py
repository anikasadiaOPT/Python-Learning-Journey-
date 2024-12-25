# Script: Understanding Indexing and Format Specifiers in Python

# Indexing: Access elements of a sequence using [] (indexing operator)
# Syntax: [start:end:step]

credit_number = "1234-5678-0987"

# Demonstrating various indexing operations
# Extract the first 4 characters
print(credit_number[0:4])  # Output: 1234
print(credit_number[:4])   # Same as above: 1234

# Extract characters from index 5 to 8
print(credit_number[5:9])  # Output: 5678

# Extract all characters from index 5 to the end
print(credit_number[5:])   # Output: 5678-0987

# Exclude the last 2 characters
print(credit_number[:-2])  # Output: 1234-5678-09

# Extract characters at every second position
print(credit_number[::2])  # Output: 134678087

# Mask credit card number except for the last 4 digits
last_digit = credit_number[-4:]
print(f"Masked Credit Card: XXXX-XXXX-{last_digit}")

# Format Specifiers: Format values using flags within curly braces {}
# Syntax: {value:flags}

# Flags:
# .(number)f  -> Round to that many decimal places (fixed point)
# :(number)   -> Allocate that many spaces
# :03         -> Allocate and zero-pad that many spaces
# :<          -> Left justify
# :>          -> Right justify
# :^          -> Center align
# :+          -> Include a plus sign for positive values
# :=          -> Place the sign at the leftmost position
# : (space)   -> Insert a space before positive numbers
# :,          -> Add a comma as a thousand separator

# Sample price values
price1 = 3000000.123445
price2 = -9140.542
price3 = 1200.123445

# Demonstrating format specifiers with f-strings
print(f"Price 1 is {price1:.1f}")  # Round to 1 decimal place
print(f"Price 1 is {price1:15}")   # Allocate 15 spaces
print(f"Price 1 is {price1:015}")  # Allocate 15 spaces with zero padding
print(f"Price 1 is {price1:<10}")  # Left justify
print(f"Price 1 is {price1:>10}")  # Right justify
print(f"Price 1 is {price1:^10}")  # Center align
print(f"Price 1 is {price1:+10}")  # Include + sign for positive values
print(f"Price 1 is {price1: }")    # Add a space before positive numbers
print(f"Price 2 is {price2: }")    # Space before the negative value
print(f"Price 1 is {price1:,}")    # Thousand separator with commas
print(f"Price 1 is {price1:+,.2f}") # Comma separator with + sign and 2 decimal places

# Note: Ensure your environment supports f-strings (Python 3.6+).
