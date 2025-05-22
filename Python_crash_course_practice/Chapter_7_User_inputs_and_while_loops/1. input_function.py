# use input() function if you want to prompt the user for input:

# The input() function pauses your program and waits for the user to enter
# some text. Once Python receives the user’s input, it assigns that input to a
# variable to make it convenient for you to work with.
# input assigns variable type as string

message = input("Type something and it will be repeated: ")
print(message)

# Type something and it will be repeated: --> prompt
# message - variable

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

# += operator takes the string that was assigned to prompt and adds
# the new string onto the end

# Using int() to accept numerical input:


number = input("what is your age? ")
print(number)

# this will assign the numerical value provided by user to number and print number.
# because of how input works, number is considered as a string.
# in order to convert it to integer type, use int()

number = int(number)

if number>=18:
    print("You're old enough to vote!")
else:
    print("Sorry! You are not old enough to vote.")

# write a program to report whether the number is a multiple of 10:

multiple = input("Please provide a number and we will check if it is a multiple of 10: ")
multiple = int(multiple)
if multiple % 10 ==0:
    print("The number you provided is a multiple of 10.")
else:
    print("The number you provided is not a multiple of 10")



