# slicing is used to work with a specific group of items in a list (aka slice)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# will print a slice of the list - from index 0 to 2 - ['charles', 'martina', 'michael']. 
# based on the specified index positions, any slice can be produced.


# If you omit the first index in a slice, Python automatically starts your
# slice at the beginning of the list

print(players[:4])
# prints from 0 to 3

## If you omit the last index in a slice, Python automatically ends your
# slice at the last of the list
print(players[2:])
#prints from 2 to last

print(players[0:4:2])
#a third argument can be used to skip items in a list when producing the slice

# looping through a slice

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Output is not presented as a list

# Here are the first three players on my team:
# Charles
# Martina
# Michael

# copying a list using slicing 
# use [:] to copy the entire list

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# the slice of the original list is a new list and is not affeccted by operations on the original list
# using friend_foods = my_foods is just associating friend_foods variable to my_foods variable



