# comprehensions allow you to create a list/set/dictionary in one line instead of multiple lines of code

# list comprehension for a list of square numbers

squares = [value**2 for value in range(1, 11)]
print(squares)

#using range to create a list of square numbers for first 10 numbers
# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)
# print(squares)