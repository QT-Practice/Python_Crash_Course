# conditional statement (aka boolean expression) - statement that can be determined to be true or false.
# if uses conditional statements to execute certain scenarios

# and/or can be used to check multiple conditions
# age_0 >= 21 and age_1 >= 21 / age_0 >= 21 or age_1 >= 21
# equality operator ==
# inequality operator !=


# checking whether a value is in a list - use in operator
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if "mushrooms" in requested_toppings:
    print (requested_toppings)

#checking whether a value is not in a list - use not in operator
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")


# if-else statements
# used when one action is to be executed for one condition and another action to be executed for another condition
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# if-elif-else - to test more than two possible situations
# use when only one condition needs to pass
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# using multiple elif blocks
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

# else is a catchall statement. you can use multiple specific conditions for a if-elif chain instead of using an else statement.

# using multiple if conditions - used when you need to check multiple conditions

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nEnjoy your pizza!")


# using if statements with lists
# can be used to perform specific tasks on specific values in a list

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

#starting with an empty list
requested_toppings = []
#checks for empty list
if requested_toppings: 
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


# using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")