# Python Collections: Lists
# A collection is a single "variable" used to store multiple values.
# Lists are ordered and mutable (changeable) collections that allow duplicate values.

# Example List of Fruits
fruits = ["Mango", "Strawberry", "Jack Fruit", "Guava", "Apple"]

# Accessing List Items
print(fruits[0])  # Output: Mango
print(fruits[1])  # Output: Strawberry
print(fruits[2])  # Output: Jack Fruit
print(fruits[3])  # Output: Guava

# Iterating Over a List
for fruit in fruits:
    print(fruit)

# Length of the List
print(len(fruits))  # Output: 5

# Check for Membership in List
print("Apple" in fruits)  # Output: True
# Note: Avoid spaces in strings unless intentional, as they are counted as characters.

# Most Common Python List Operations

# Example List of Numbers
num = [1, 2, 3, 4, 5, 5, 6, 7, 8]

# append(): Add an item to the end of the list
num.append(10)
print(num)  # Output: [1, 2, 3, 4, 5, 5, 6, 7, 8, 10]

# extend(): Add elements from another list to the end of the current list
num.extend([15, 20])
print(num)  # Output: [1, 2, 3, 4, 5, 5, 6, 7, 8, 10, 15, 20]

# insert(): Insert an item at a specific index
num.insert(3, 1)  # Inserts '1' at index 3
print(num)  # Output: [1, 2, 3, 1, 4, 5, 5, 6, 7, 8, 10, 15, 20]

# remove(): Remove the first occurrence of a value
num.remove(10)
print(num)  # Output: [1, 2, 3, 1, 4, 5, 5, 6, 7, 8, 15, 20]

# pop(): Remove and return an element by its index
num.pop(5)  # Removes the element at index 5
print(num)  # Output: [1, 2, 3, 1, 4, 5, 6, 7, 8, 15, 20]

# Searching and Counting in Lists

# index(): Get the index of the first occurrence of a value
print(num.index(3))  # Output: 2

# count(): Count occurrences of a value in the list
print(num.count(19))  # Output: 0 (value not found)
print(num.count(1))   # Output: 2 (value occurs twice)

# Sorting and Reversing Lists

# sort(): Sort the list in place (ascending order by default)
num.sort()
print(num)  # Output: [1, 1, 2, 3, 4, 5, 6, 7, 8, 15, 20]

# sorted(): Return a new sorted list without altering the original
sorted_list = sorted(num, reverse=True)  # Sorts in descending order
print(sorted_list)  # Output: [20, 15, 8, 7, 6, 5, 4, 3, 2, 1, 1]

# reverse(): Reverse the list order in place
num.reverse()
print(num)  # Output: [20, 15, 8, 7, 6, 5, 4, 3, 2, 1, 1]

# Basic List Operations

# Slicing: Extract parts of the list
sub_list = num[::2]  # Every second element
print(sub_list)  # Output: [20, 8, 6, 4, 2, 1]

# List Comprehension: Create a new list using a compact loop
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Length of a List
print(len(num))  # Output: 11 (length of the list)

# Membership Check
if 10 in num:
    print("Found")
else:
    print("Not Found")  # Output: Not Found (10 was removed earlier)
