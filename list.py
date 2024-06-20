# a list is a versatile data structure that allows you to store a collection of items in a single variable.
# Lists are ordered, mutable, and con contain elements of different data types.

# Create a List
# Empty list
empty_list = []

# List of integers
int_list = [1, 2, 3, 4, 5]

# List of strings
string_list = ["apple", "banana", "cherry"]

# List of mixed data types
mixed_list = [1, "apple", True]

# Accessing Elements
fruits = ["apple", "banana", "cherry"]

# Access the first element
print(fruits[0])

# Access the last element
print(fruits[-1])

# Slicing a List
# list[start:stop:step]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Elements from index 2 to 5
print(numbers[2:6])

# Every second element
print(numbers[::2])

# Elements from index 1 to the end
print(numbers[1:])

# Elements up to index 4
print(numbers[:5])

# Modifying a List
# List are mutable, meaning you can change their content
fruits2 = ["apple", "banana", "cherry"]

# Change the second element
fruits2[2] = "blueberry"
print(fruits2)

# Add a new element to the end
fruits2.append("date")
print(fruits2)

# Insert an element at a specific position
fruits2.insert(1, 'blackberry')
print(fruits2)

# Remove an element by value
fruits2.remove("blackberry")
print(fruits2)

# Remove an element by index
del fruits2[2]
print(fruits2)

# Remove and return the last element
last_fruit = fruits2.pop()
print(last_fruit)
print(fruits2)

# List Operations
# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)

# Repetition
repeated_list = [1, 2, 3] * 3
print(repeated_list)

# Membership testing
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("date" not in fruits)
print("cherry" not in fruits)

# List comprehension
# List comprehension provide a concise way to create lists.
# Simple list comprehension
squares = [x**2 for x in range(10)]
print(squares)

# List comprehension with condition
even_squares = [x** 2 for x in range(10) if x % 2 == 0]
print(even_squares)

# Useful list methods
numbers = [1, 2, 3, 4, 5]

# Find the length of the list
print(len(numbers))

# Find the maximum value
print(max(numbers))

# Find the minimum value
print(min(numbers))

# Count the occurrences of an element
print(numbers.count(3))

# Sort the list
numbers = [2, 1, 4, 3, 5] # don't modify the original list
print(sorted(numbers));

numbers.sort() # modify the original list
print(numbers)

# Reverse the list
numbers.reverse()
print(numbers)

# Copy a list
numbers_copy = numbers.copy()
print(numbers_copy)

# Iterating over a list
# You an iterate over the elements of a list using a `for` loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    
# Nested Lists
nested_list = [[1, 2, 3], ["a", "b", "c"], [True, False]]

# Access a element in a nested list
print(nested_list[0][1])
print(nested_list[1][1])

names = ["Nina", "Max", "Nina"]
print(names)

# Find the index of item in the list
pos = names.index("Nina")
names[pos] = "Soup"
print(names)