# use while loop to keep a program running as long as the defined condition is true

# The for loop takes a collection of items and executes a block of code once for each item in the collection. 
# In contrast, the while loop runs as long as, or while, a certain condition is true.

# current_number = input("Please provide a number below 100 and we will count up to the number from 0: ")
# current_number = int(current_number)
# while 0> current_number < 100:
#     new_number = current_number-1
#     addition = current_number+new_number
#     current_number=current_number-1
#     print(addition)

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# defining a quit value to let the user choose when to quit:

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# We define message as an empty string, "", so Python has something to check the first time it reaches the while line. 
# The first time the program runs and Python reaches the while statement, it needs to compare the value of message to 'quit', 
# but no user input has been entered yet. If Python has nothing to compare, it won’t be able to continue running the program.

# the below modified program uses if condition to make sure that quit will not be repeated to the user

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# using a flag to keep track of multiple conditions:

# For a program that should run only as long as many conditions are true, 
# you can define one variable that determines whether or not the entire program is active. 
# This variable, called a flag, acts as a signal to the program. 
# We can write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False. 

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# since active is set to True, while loop will be executed until active = False.
# active is set to False when message == 'quit'

# using break to exit the loop:

# To exit a while loop immediately without running any remaining code in the loop, 
# regardless of the results of any conditional test, use the break statement. 
# The break statement directs the flow of your program; 
# you can use it to control which lines of code are executed and which aren’t 
# so the program only executes code that you want it to, when you want it to.

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# A loop that starts with while True will run forever unless it reaches a
# break statement. The loop in this program continues asking the user to enter
# the names of cities they’ve been to until they enter 'quit'. When they enter
# 'quit', the break statement runs, causing Python to exit the loop.

# You can use the break statement in any of Python’s loops. 
# For example, you could use break to quit a for loop that’s working through a list or a dictionary.


# using continue in a loop:

# Rather than breaking out of a loop entirely without executing the rest of its code, 
# you can use the continue statement to return to the beginning of the loop, based on the result of a conditional test.

number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)

# If the modulo is 0 (which means current_number is divisible by 2), 
# the continue statement tells Python to ignore the rest of the loop and return to the beginning. 
# If the current number is not divisible by 2, the rest of the loop is executed and Python prints the current number.

# use while loop to modify a list

# A for loop is effective for looping through a list, 
# but you shouldn’t modify a list inside a for loop because Python will have trouble keeping track of the items in the list. 
# To modify a list as you work through it, use a while loop. 
# Using while loops with lists and dictionaries allows you to collect, store, and organize lots of input to examine and report on later.

# moving items from one list to another

# Start with users that need to be verified, and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# The while loop runs as long as the list unconfirmed_users is not empty.
# pop() is used to remove users from the list and is assigned to variable current_user.
# current_user is appended to confirmed_users list.

# for loop is used to display all users in confirmed_user after while loop execution is complete.

#use while loop to remove all instances of a value from a list

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# filling a dictionary with user input using while loop

responses = {}
# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # Store the response in the dictionary.
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
print(f"{name} would like to climb {response}.")