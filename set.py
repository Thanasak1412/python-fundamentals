# A set is an unordered collection of unique elements.

# Creating a Set
# You can create a set by using curly braces `{}` or the `set()` function
# Using curly braces
numbers = {1, 2, 3, 4, 5}
print(numbers)

# Using the set() function
fruits = set(["apple", "banana", "berry"])
print(fruits)

# Adding Elements
# Adding single element
fruits.add("blueberry")
print(fruits)

# Adding multiple elements
fruits.update(["grape", "mango"])
print(fruits)

# Removing elements
# Removing an element using `remove()`` (raises KeyError if the element does not exist)
fruits.remove("grape")
print(fruits)

# Removing an element using `discard()` (does not raise an error if the element does not exist)
fruits.discard("mango")
print(fruits)

# Removing arbitrary element using `pop()`
removed_element = fruits.pop()
print(removed_element)
print(fruits)

# Set operations

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1.union(set2)
print(union_set)

# Intersection
intersection_set = set1.intersection(set2)
print(intersection_set)

# Difference
difference_set = set1.difference(set2)
print(difference_set)

# Symmetric difference
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)

# Checking membership
print(1 in set1)
print(5 in set1)

# Checking if a set is a subset
print({1, 2}.issubset(set1))

# Checking if a set is a superset
print(set1.issuperset({1, 2}))

# Clear a set
set1.clear()
print(set1)

# Immutable sets
frozen_set = frozenset([1, 2, 3, 4])
print(frozen_set)

# Trying to add or remove elements will raise an error
frozen_set.add(5)