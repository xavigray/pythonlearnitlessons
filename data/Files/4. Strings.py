# String in Python
greenting = "Hello, world!"
name = "Alice"

# Length of a string
# Using len() function to get the length of a string
print(len(greenting)) # Output: 13

#Indexing
print(greenting[0]) # Output: H
print(greenting[2]) # Output: l
print(name[-1]) # Output: e

# Slicing
# The syntax is string[start:end:step]
print(greenting[0:5]) # Output: Hello
print(name[1:3]) # Output: li
print(greenting[::-1]) # Output: !dlrow ,olleH
print(greenting[::-2]) # Output: !lo olH

# Concatenation
full_name = name + 'Wonderland'
full_name_space = name + ' ' + 'Wonderland'
print(full_name)
print(full_name_space)

# Repetition with '*'
chant = name*3
print(chant)    # Output: 'AliceAliceAlice'

# Using String Methods
print(greenting.upper())    # Output: HELLO, WORLD!
print(name.lower())    #Output: alice
print(name.replace('l','x'))   # Output: Axice
