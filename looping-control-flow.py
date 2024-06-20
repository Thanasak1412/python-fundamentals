"""Looping
    Looping allows you to execute a block of code multiple times. Python supports two main types of loops
"""

# For loop: Iterates over a sequence (such as a list, tuple, dictionary, set, or string).
colors = ["Red", "Blue", "Green"]

for color in colors:
    print(color)
    
print(color)

my_dict = { "one": 1, "two": 2, "three": 3 }

for label, value in my_dict.items():
    print(label, value)
    
for label in my_dict:
    print(f"value: {my_dict[label]} of {label} key")
    
num = 10

for i in range(0, num, 2):
    print(i)
    
# While loop: Repeats as long as a certain condition is true.
count = 0
max = 20

while count <= max:
    print(count)
    count += 2
    
"""Control Flow
    Control flow statements allow you to control the execution of your program.
    Python provides several control flow statements:
    1. if, elif, else: Conditional statements that execute different blocks of code based on conditions.
    2. break: Exits the loop.
    3. continue: Skips the rest of the code inside the loop for the current iteration and jumps to the next iteration.
    4. pass: Does nothing and can be used as a placeholder.
"""

# if, elif, else
x = 10
if x < 0:
    print("Negative number")
elif x == 0:
    print("Zero")
else:
    print("Positive number")
    
# break
for i in range(10):
    if i == 5:
        break
    print(i)
    
# continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    
for i in range(10):
    if i % 2 == 0:
        pass # Do noting
    else:
        print(i)
        
# Combining loops and control flow
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")