# Sets = {} unordered and immutable, but Add/Remove OK. NO duplicates

# Creating Sets
num = {2, 3, 4, 5, 6, 7}  # Using curly braces to define a set
print("Original Set:", num)

another_num = set([1, 2])  # Using the set() function
print("Another Set:", another_num)

# Adding and Removing Elements
# add(): Adds a single element to the set.
num.add(9)
print("Set after adding 9:", num)

# remove(): Removes a specific element (raises an error if the element is not present).
num.remove(5)
print("Set after removing 5:", num)

# discard(): Removes a specific element (does not raise an error if the element is not present).
num.discard(2)
print("Set after discarding 2:", num)

# pop(): Removes and returns an arbitrary element.
popped_element = num.pop()
print("Set after pop():", num)
print("Popped Element:", popped_element)

# Set Operations
num1 = {1, 2, 3, 4, 5, 6}
num2 = {5, 6, 7, 8, 9, 10, 11, 12}

# union() |: Returns all unique elements from both sets.
union_set = num1 | num2
print("Union of num1 and num2:", union_set)

# intersection() &: Returns common elements between sets.
intersection_set = num1 & num2
print("Intersection of num1 and num2:", intersection_set)

# difference() -: Returns elements in the first set but not in the second.
difference_set = num1 - num2
print("Difference (num1 - num2):", difference_set)

# symmetric_difference() ^: Returns elements in either set but not in both.
sym_diff_set = num1 ^ num2
print("Symmetric Difference of num1 and num2:", sym_diff_set)

# Subset and Superset
# issubset(): Checks if all elements of the set are in another set.
is_subset = num1.issubset(num2)
print("Is num1 a subset of num2?", is_subset)

# issuperset(): Checks if a set contains all elements of another set.
is_superset = num1.issuperset(num2)
print("Is num1 a superset of num2?", is_superset)

# Membership Testing
if 3 in num1:
    print("3 is in num1.")
else:
    print("3 is not in num1.")
