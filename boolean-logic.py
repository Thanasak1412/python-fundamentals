"""Truthy values
Any value that is not falsy is considered truthy. This includes:
1. `True`
2. Non-zeo numeric: `1`, `-1`, `3.14`
3. Non-empty collections and sequences: `'hello'`, `[1, 2, 3]`, `{"a", 1}`, `{1, 2, 3}`, `(1, 2, 3)`
"""

# Using Truthiness in condition statements

# Example with a list
my_list = [1, 2, 3]

if my_list:
    print("The list not empty.")
else:
    print("The list is empty.")
    
# Example with a string
my_string = ""

if my_string:
    print("The string is not empty.")
else:
    print("The string is empty.")
    
"""Custom Truthiness
You can define custom truthiness for you classes by implementing the `__bool__` and `__len__` methods.
"""

class MyClass:
    def __init__(self, value):
        self.value = value
        
    def __bool__(self):
        return self.value > 0
    
    def __len__(self):
        return self.value
    
obj = MyClass(0)
print(bool(obj))

obj.value = 10
print(bool(obj))

print("cat" > "bat")