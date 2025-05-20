# dictionary contains a collection of key-value pairs.
# each key is connected to a value and you can access the value using the key.
# a key can be a number, string, list or another dictionary.
# both key and value should be in quotations
# Every key is connected to its value by a colon, and individual key-value pairs are separated by commas.
# dictionaries retain the order in which they were defined

# list - []
# set - {}
# tuple - ()
# dictionary - {"key1": "value1" , "key2": "value2" }

aliens_0 = {
    "color" : "green",
    "shape" : "round"
}

print (aliens_0["color"])
print (aliens_0["shape"])

# Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# modifying a key value in dictionary
alien_0['color'] = 'yellow'
print(alien_0['color'])
print(alien_0)
print(f"The alien is now {alien_0['color']}")

# deleting a key/value pair with del.
# deletion is permanent
aliens_0 = {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
print(aliens_0)
del aliens_0['x_position']
print(aliens_0)


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# using get() method to access values
# For dictionaries specifically, you can use the get() method to set
# a default value that will be returned if the requested key doesn’t exist.
# The get() method requires a key as a first argument. As a second optional
# argument, you can pass the value to be returned if the key doesn’t exist.

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# If there’s a chance the key you’re asking for might not exist, 
# consider using the get() method instead of the square bracket notation.
# If you leave out the second argument in the call to get() and the key doesn’t exist,
# Python will return the value None. The special value None means “no value exists.”
# This is not an error: it’s a special value meant to indicate the absence of a value.
