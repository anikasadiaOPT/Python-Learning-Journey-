"""
Shopping Cart Program
This program allows users to add food items and their prices to a virtual shopping cart.
Users can view the total cost of their cart and exit by entering 'q'.
"""

# Initialize variables
foods = []  # List to store food items
prices = []  # List to store food prices
total = 0  # Variable to store the total cost

print("Welcome to the Shopping Cart Program!")
print("Add items to your cart and view the total cost. Enter 'q' to quit.\n")

# Main loop to collect food items and prices
while True:
    food = input("Enter a food to buy (q to Quit): ").strip()
    
    # Check if the user wants to quit
    if food.lower() == "q":
        break
    
    # Get the price of the food item
    try:
        price = float(input(f"Enter the price of {food}: $").strip())
        foods.append(food)
        prices.append(price)
    except ValueError:
        print("Invalid price. Please enter a numeric value.\n")
        continue

# Print the shopping cart summary
print("\n------ MY SHOPPING CART ------")
for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]:.2f}")

# Calculate the total price
total = sum(prices)
print(f"\nYour total price is: ${total:.2f}")

print("\nThank you for using the Shopping Cart Program!")
