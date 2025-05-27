# a function does not have to display its output. 
# return value - value that is returned by a function 
# return statement is used to take the value from function and to pass it back

# returning a simple value

def get_formatted_name(first_name, last_name):
    """Function used to create a formatted full name

    Args:
        first_name 
        last_name 
    """
    full_name = f"{first_name} {last_name}"
    return(full_name.title())

scientists = get_formatted_name('albert', 'einstein')
print(scientists)

# making an argument optional using default values

#middle_name default value is empty
def formatted_name_with_default(first_name, last_name, middle_name=''):
    """Function used to create a formatted full name with a default middle name
    Args:
        first_name 
        last_name 
        middle_name 
    """
    #if middle name is present, middle_name is returned in full_name
    if middle_name == True: 
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

# no middle name is provided
scientist = formatted_name_with_default('albert', 'einstein')
print(scientist)

# middle name is provided
scientist_with_middle_name = formatted_name_with_default('albert', 'einstein', 'thomas')
print(scientist_with_middle_name)

# returning a dictionary


def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    # defining a dictionary named person 
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# using default values to create a dictionary

# default value for age is None
def build_person_with_default_values(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}

    # if value of age is provided
    if age:
        person['age'] = age
    return person


musician = build_person_with_default_values('jimi', 'hendrix', age=27)
print(musician)
