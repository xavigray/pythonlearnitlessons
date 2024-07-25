# Dictionay in Python
# Creating dictionaries

#person = {'name: ', 'John', 'age: ','30', 'city: ','New York'} # incorrect
person = {'name' : 'John', 'age' : '30', 'city' : 'New York'}

# Accessing dictionary values
print(person['name'])   # Output: John
print(person['age'])    # Output: 30


# Adding and modifying dictionary values
person['email'] = 'john@example.com'    # Adding a new key-value pair
person['age'] = 33  # Modifying an existing value

# Removing dictionary items
del person['city']  # Removing the 'city' key-value pair
age =  person.pop('age') # Removing the 'age' key-value pair

# Iterating over dictionaries
for key in person:
    print(key,person[key])  # Itarating over keys and printing key-value pair
# for value in person():    # Incorrect
for value in person.values():
    print(value)    # Itarating over values
for key, value in person.items():
    print(key, value)   # Iterating over key-value pairs