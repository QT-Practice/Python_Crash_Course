
# looping through a dictionary using for loop

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

# looping through key and value using .items() approach. both key and value are accessed and both values can be printed.
for key, value in favorite_languages.items():
    print(f"\nName: {key}")
    print(f"Favorite language: {value}")

# looping through key using .keys() approach. only key is accessed.
for key in favorite_languages.keys():
    print(key.title())

# using sorted function to loop through keys 
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# looping through value using .values() approach. only value is accessed
for value in favorite_languages.values():
    print(value.title())

# Set - collection in which each item has to be unique.

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# using set to print only unique items from values
# Note: Dictionary has key-value pairs, set does not. Both use {}.