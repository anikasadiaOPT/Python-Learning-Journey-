# Dictionaries Demonstration

# --- Overview ---
# A dictionary is a collection of key-value pairs, which is:
# 1. Ordered (from Python 3.7 onwards)
# 2. Changeable
# 3. Does not allow duplicate keys

# Example Dictionary: Country Capitals
capitals = {
    "USA": "Washington D.C",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# --- Dictionary Operations ---

# Get the capital of a country using the .get() method
# This method safely retrieves the value for a key without raising a KeyError if the key is absent.
print(capitals.get("USA"))  # Output: Washington D.C

# Check if a key exists in the dictionary
if capitals.get("Japan"):
    print("That capital exists.")
else:
    print("That capital doesn't exist.")

# Add new key-value pairs to the dictionary using .update()
capitals.update({"Germany": "Berlin"})
capitals.update({"Bangladesh": "Dhaka"})

# Retrieve all keys in the dictionary
keys = capitals.keys()
print("Keys:", keys)

# Iterate through all keys in the dictionary
print("Keys in the dictionary:")
for key in capitals.keys():
    print(key)

# Retrieve all values in the dictionary
values = capitals.values()
print("\nValues:", values)

# Iterate through all values in the dictionary
print("Values in the dictionary:")
for value in capitals.values():
    print(value)

# Additional Operations (Commented for reference):
# capitals.pop("China")       # Remove a specific key-value pair
# capitals.popitem()          # Remove the last inserted key-value pair
# capitals.clear()            # Clear the entire dictionary

# End of Script
