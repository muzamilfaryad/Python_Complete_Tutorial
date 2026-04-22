


coordinates = (10.0, 20.0)
print(coordinates[0])  # Output: 10.0
print(coordinates[1])  # Output: 20.0
# Tuples are immutable, so the following line would raise an error:
# coordinates[0] = 15.0  # This will raise a TypeError
# However, you can create a new tuple by concatenating existing tuples:
new_coordinates = coordinates + (30.0,)
print(new_coordinates)  # Output: (10.0, 20.0, 30.0)
# You can also unpack tuples into variables:
x, y = coordinates
print(x)  # Output: 10.0
print(y)  # Output: 20.0

print(type(coordinates))  # Output: <class 'tuple'>
# Tuples can contain different data types
mixed_tuple = (1, "Hello", 3.14)
print(mixed_tuple)  # Output: (1, 'Hello', 3.14)


print(coordinates[0])  # Output: 10.0
print(coordinates[1])  # Output: 20.0



# #immutable
# coordinates[1] = 50
# print(coordinates[1])  # This will raise a TypeError because tuples are immutable


# Tuples Inside Lists
# You can have tuples inside lists
list_of_tuples = [(1, 2), (3, 4), (5, 6)]
print(list_of_tuples)  # Output: [(1, 2), (3, 4), (5, 6)]
# You can access elements of the tuples inside the list
print(list_of_tuples[0])  # Output: (1, 2)
print(list_of_tuples[0][0])  # Output: 1
print(list_of_tuples[0][1])  # Output: 2

list_of_tuples.append((7, 8))
print(list_of_tuples)  # Output: [(1, 2), (3, 4), (5, 6), (7, 8)]

