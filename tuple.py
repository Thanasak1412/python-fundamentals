my_tuple = (1, 2, 3)
print(my_tuple)

# count: returns the number of times a specified value occurs in a tuple.
my_tuple = (1, 2, 3, 1, 1)
print(my_tuple.count(1))

# index: Searches the tuple for a specified value and returns the position of where it was found.
my_tuple = (1, 2, 3)
print(my_tuple.index(2))

# Immutability
# Tuples are immutable, meaning their elements cannot be changed after assignment.
my_tuple = (1, 2, 3)
my_tuple[1] = 4

# Using Tuples
# Tuples are useful in many situations where you want to ensure the data remains unchanged.
# They can also be used as keys in dictionaries (unlike lists)
# Tuples as dictionary keys
locations = {
    (35.6895, 139.6917): "Tokyo",
    (40.7128): "New York"
}

print(locations[(35.6895, 139.6917)])

# Unpacking Tuples
# Tuples can be unpacked into variables.
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)
print(b)
print(c)

# This feature is particularly useful in returning multiple values from a function.
def get_coordinate():
    return (35.6895, 139.7917)

latitude, longitude = get_coordinate()

print(latitude)
print(longitude)