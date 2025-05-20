# Sometimes you’ll want to store multiple dictionaries in a list, 
# or a list of items as a value in a dictionary. This is called nesting. 
# You can nest dictionaries inside a list, a list of items inside a dictionary, 
# or even a dictionary inside another dictionary.

# list of dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# a list in a dictionary

pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

# using a for loop within a for loop to access all keys and values
favorite_languages = {
'jen': ['python', 'rust'],
'sarah': ['c'],
'edward': ['rust', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# a dictionary within a dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")