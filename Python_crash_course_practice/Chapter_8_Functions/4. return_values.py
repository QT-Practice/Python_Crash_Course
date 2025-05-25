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

