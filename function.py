# Simple function
def add_numbers(a, b):
    """This function takes two numbers and returns their sum.

    Args:
        a (_number_): _number to computes_
        b (_number_): _number to computes_

    Returns:
        _number_: _the computed sum of a and b_
    """
    
    result = a + b
    return result

sum_result = add_numbers(5, 10)
print(sum_result)

# Function with default parameters
def greet(name, greeting="Hello"):
    
    """This function greets a person with the provided greeting.

    Args:
        name (_string_): name of person to greeting.
        greeting (_string_): greeting message

    Returns:
        _string_: _greeting message_
    """
    
    return f"{greeting}, {name}"
    
# Call with both arguments
print(greet("Alice", "Hi"))

# Call with only the name argument
print(greet("Bob"))

# Function with Variable Number of arguments
def multiply(*args):
    """This function multiples an arbitrary number of numbers.

    Returns:
        _number_: _the result of multiply number from arguments_
    """
    
    result = 1
    for num in args:
        result *= num
        
    return result

# Call with multiple arguments
print(multiply(2, 3, 4))

# Call with a different set of arguments
print(multiply(5, 10))