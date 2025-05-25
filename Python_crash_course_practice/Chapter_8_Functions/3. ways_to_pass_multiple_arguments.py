# function definition can have multiple parameters.
# function call may need multiple arguments

# ways to send multiple arguments

# 1. positional arguments - arguments passed in function call need to be in the same order as parameters defined in the function

def pet(animal_type, pet_name):
    """Display pet informatio"""
    print(f"I have a pet {animal_type}")
    print(f"My pet's name is {pet_name.title()}")

pet('dog', 'jimmy')
pet('hamster', 'harry')

# a function can be called multiple times
# note: order matters in positional arguments. pet('harry', 'hamster') will display output, but would read funny.

# keyword arguments - name/value pair that you pass to a function.
# Youdirectly associate the name and the value within the argument, so when you
# pass the argument to the function, there’s no confusion (you won’t end up
# with a harry named Hamster). Keyword arguments free you from having
# to worry about correctly ordering your arguments in the function call, and
# they clarify the role of each value in the function call.

def pet(animal_type, pet_name):
    """Display pet informatio"""
    print(f"I have a pet {animal_type}")
    print(f"My pet's name is {pet_name.title()}")

pet(animal_type='dog', pet_name='jimmy')
pet(pet_name='harry', animal_type='hamster')

# while using keyword arguments, position does not matter, but be sure to use the same parameters in the function call to avoid errors

# defining default values for a parameter

# When writing a function, you can assign a default value for a parameter. 
# If an argument for a parameter is provided in the function call, Python uses the argument value. 
# If not, it uses the parameter’s default value.

def pet(pet_name, animal_type = 'dog'):
    """Display pet informatio"""
    print(f"I have a pet {animal_type}")
    print(f"My pet's name is {pet_name.title()}")

pet(pet_name='jimmy')

# animal_type parameter has a default value assigned to it as dog in function. animal_type = 'dog'
# when animal_type argument is not passed in function call, default value is assumed
# note: the first parameter cannot be a default value. 

pet('jimmy') 

# is the same as pet(pet_name='jimmy')

pet(pet_name='harry', animal_type='hamster')

#since animal_type value is specified, default value is ignored.


