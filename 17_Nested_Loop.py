# Nested Loops Example
# A loop within another loop (outer and inner loops).

# Example 1: Printing Numbers with Two Nested Loops
# Outer loop: iterates 3 times.
# Inner loop: iterates 10 times, printing numbers from 1 to 10 in each iteration of the outer loop.

for i in range(3):  # Outer loop (3 times)
    for j in range(1, 11):  # Inner loop (printing numbers from 1 to 10)
        print(j, end=" ")
    print()  # Newline after printing numbers for each outer loop iteration

# Example 2: Create a Grid of Symbols
# Asking the user for rows, columns, and a symbol to print in a grid format.
rows = int(input("Enter the rows: "))
col = int(input("Enter the columns: "))
symbol = input("Enter the symbol: ")

for i in range(rows):  # Outer loop: iterates over each row
    for j in range(col):  # Inner loop: iterates over each column in the current row
        print(symbol, end=" ")  # Print the symbol in each column without newline
    print()  # Newline after completing each row

# Example 3: Multiplication Table using Nested Loops
# This nested loop generates a multiplication table up to 5x5.

print("Multiplication Table (5x5):")
for i in range(1, 6):  # Outer loop for rows (1 to 5)
    for j in range(1, 6):  # Inner loop for columns (1 to 5)
        print(i * j, end="\t")  # Print the product of the current row and column values
    print()  # Newline after each row

# Example 4: Pattern Printing with Nested Loops
# This example prints a right triangle pattern of stars.

height = int(input("Enter the height of the triangle: "))

for i in range(1, height+1):  # Outer loop controls the number of rows (1 to height)
    for j in range(i):  # Inner loop controls the number of stars in each row (based on row number)
        print("*", end=" ")  # Print a star in each column without newline
    print()  # Newline after each row

# Example 5: Generating a 2D Matrix (List of Lists)

rows = int(input("Enter the number of rows for the matrix: "))
cols = int(input("Enter the number of columns for the matrix: "))
matrix = []

for i in range(rows):  # Outer loop: iterates for each row in the matrix
    row = []  # Initialize a new row for each iteration
    for j in range(cols):  # Inner loop: iterates for each column in the current row
        row.append(int(input(f"Enter value for row {i+1}, col {j+1}: ")))  # Add value to the row
    matrix.append(row)  # Add the completed row to the matrix

# Print the matrix
print("The generated matrix:")
for row in matrix:  # Outer loop: iterate through rows in the matrix
    for item in row:  # Inner loop: iterate through each item in the row
        print(item, end=" ")  # Print each value in the row
    print()  # Newline after each row
