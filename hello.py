print("Hello, World!")

# Integer
age = 25

# Float
price = 19.99

# String
name = "Alice"

# Boolean
is_student = True

# print(type(age))
# print(type(price))
# print(type(name))
# print(type(is_student))

# Lists
fruits = ['apple', 'banana', 'cherry']
print(fruits)

fruits[1] = 'lemon'

print(fruits[0])
print(fruits)

colors = ('blue', 'red', 'yellow')
print(colors)
colors[1] = 'green'
print(colors)

person = {
    "name": "John",
    "age": 30,
    "city": "New york"
}

person["phone"] = "0987654321"

person[555] = "Test key integer"

person[True] = "Test key boolean"

print(person)

person['name'] = 'Doe'

print(person['name'])

# Conditional
# Python uses `if`, `elif`, and `else` for conditional statements
x = 10
if x > 5:
    print('x is greater than 5')
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
    
# Loops
# There are two main types of loops in Python: `for` loops and `while` loops.
# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
    
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))

# Classes and Objects
# Python is an object-oriented programming language, meaning it allows for the creation of classes and objects.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person1 = Person()
print(person1.greet())

x = 10
x = "10"
x = True