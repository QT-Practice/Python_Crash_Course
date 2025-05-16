# When you want to do the same action with every item in a list, 
# you can use Python’s for loop.

cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
    print (car)
    print (f"{car.title()} is one of my previously owned cars")

# range function - increments automatically

for value in range(1,10):
    print (value)

# range (10) - starts from 0 and counts till 9

# using range() to create a list of numbers

numbers = list(range (11))
print (numbers)

# skipping numbers in a range - use a third argument to be used as step size when generating numbers

even_numbers = list(range(0,11,2))
print (even_numbers)

#using range to create a list of square numbers for first 10 numbers
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

