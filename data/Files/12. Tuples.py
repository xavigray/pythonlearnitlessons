# Tuples. Tuples are inmutable
# Creating tuples
# Empty tuples
empty_tuples = ()
# Tuple with mixed data types
person = ("John", 25, "New York")
# Tuple without parentheses
numers = 1,2,3,4,5,6

# Accesing tuple elements
print(person[0])    # Output: "John"
print(person[1])    # Output: "25"
print(person[-1])   # Output: "New York" (negative indexing)

# Tuple inmutability
#numbers[0] = 10 # Raises a TypeError

new_numbers = numers + (7, 8)
print(new_numbers)  # Output: (1,2,3,4,5,6,7,8)

# Tuple Packing and Unpacking
# Tuple packing
coordinates  = 10, 20, 30
# Tuples unpacking
x, y, z = coordinates
print(x)    # Output: 10
print(y)    # Output: 20
print(z)    # Output: 30

# Tuples Methods
# Count(elements)
# index(elements)
tuples_count = 1,2,2,2,3,3,5
print(tuples_count.count(2))    # Ouptut: 3
print(tuples_count.count(3))    # Output: 2

# Tuple as Return Values
def get_name_and_age():
    name = "Alice"
    age = 25
    return name, age
result =  get_name_and_age()
print(result)

name, age = get_name_and_age()
print(name)
print(age)





