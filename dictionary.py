# Creating a dictionary
nums = { "one": 1, "two": 2, "three": 3 }

person = dict({
    "name": "john",
    "age": 30,
    "city": "New York",
})

print(person)

# Accessing values
print(nums.get("four", "default value"))
print(person["name"])

# Adding or updating a value
person["email"] = "john@gmail.com"
person["age"] = 31

print(person)

# Deleting key-value pair
del person["age"]
print(person)

# Looping through keys and values
for key, value in person.items():
    print(key, value)

# Checking if a key exists
if "name" in person:
    print("Name is present in the dictionary")
    
# Getting the list of keys or values
nums_key = nums.keys()

print(nums_key)

nums_value = nums.values()
print(nums_value)

# Clearing all items
person.clear()

print(person)

"""Advanced dictionary method
    update(): Merges another dictionary into the current dictionary.
    setdefault(): Inserts a key with specified value if the key is not already present.
    Dictionary comprehension: Allows the creating the dictionaries in a concise way.
"""
# Updating update()
person.update({ "city": "Los Angeles", "phone": "123-456-7890" })
print(person)

# Using setdefault()
person.setdefault("name", "John")
print(person)

# Dictionary comprehension
squares = {x: x**2 for x in range(6)}
print(squares)

# Dictionaries are powerful and versatile data structure in Python, make them suitable for a wide range of application.