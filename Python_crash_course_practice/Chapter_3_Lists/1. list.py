# A list is a collection of items in a particular order. 
# In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas. 
# Note: Index positions start at 0, not 1. -1 is used to denote the last index. -2 is the one before the last.

stores = ["amazon", "costco", "bestbuy", "wegmans"]
print (stores)

# Lists are ordered collections, so you can access any element in a list by
# telling Python the position, or index, of the item desired.

print (stores[0].title())

# Modifying, adding or removing elements

# modifying
stores[-1] = "target"
print (stores)

# appending
# append adds to the end of the list. to insert, use insert
stores.append("target")
print (stores)

# insert
stores.insert(-2, "krogers")
print (stores)

# remove with del
# if you know the position of the item, use del
del stores[-2]
print (stores)

# remove with pop
# The pop() method removes the last item in a list, but it lets you work with that item after removing it.
# when you want to delete an item from a list, and not use that item in any way, 
# use the del statement; if you want to use an item as you remove it, use the pop() method.

stores_popped = stores.pop()
print (stores_popped)
print (f"{stores_popped} is declining in popularity")
print (stores)

# remove with remove()
# If you only know the value of the item you want to remove, youcan use the remove() method.

print (stores)
stores.append("target")
stores.insert(-2, "walmart")
stores.remove("walmart")
print(stores)

# Note: The remove() method deletes only the first occurrence of the value you specify. 
# If there’s a possibility the value appears more than once in the list, 
# you’ll need to use a loop to make sure all occurrences of the value are removed.

# sorting a list permanently with sort() method.

print (stores)
stores.sort()
print (stores)
stores.sort(reverse=True)

# stores = ["amazon", "costco", "bestbuy", "wegmans"]
# print (stores)
# sorted = stores.sort()
# print (sorted)
# sorted returns none. why?


# sorting a list temporarily with sorted() method.

cars = ['bmw', 'audi', 'toyota', 'subaru']
print (cars)
print (sorted(cars))

# print a list in reverse order. does not sort
# changes list order permanently. reverse again to restore

print (cars)
cars.reverse()
print (cars)
cars.reverse()
print(cars)

# find length of list with len

len(cars)



