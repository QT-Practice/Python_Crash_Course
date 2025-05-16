# tuples - list that cannot change (immutable list). use tuples when you do not want the value to be changed, unlike lists.

# Tuples: Ordered, immutable, allow duplicates, support indexing. individual elements can be accessed.
# Sets: Unordered, mutable, only unique elements, no indexing. individual elements can not be accessed.

# list - []
# set - {}
# tuple - ()

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print (dimensions)

# dimensions[0] = 250 will produce error since tuple is immutable and value cannot be changed

#Tuples are technically defined by the presence of a comma; 
# the parentheses make them look neater and more readable. 
# If you want to define a tuple with one element, you need to include a trailing comma:
# my_t = (3,)

# looping through a tuple
for dimension in dimensions:
    print(dimension)

# over writing a tuple

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

#original tuple is being overwritten with different values
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)