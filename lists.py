friends = ["Rolf", "Bob", "Anne", "Charlie", "Jen", "Sarah", "Adam"]
print(friends.sort())
print(friends)  
# Full list

print(friends[0])  
# First element: Rolf

print(friends[1])  
# Second element: Bob

print(friends[2])  
# Third element: Anne

print(friends[-1])  
# Last element: Adam

print(friends[-2])  
# Second last element: Sarah

print(friends[-3])  
# Third last element: Jen

print(friends[0:2])  
# Elements from index 0 to 1: ['Rolf', 'Bob']

print(friends[1:])  
# From index 1 to end: ['Bob', 'Anne', 'Charlie', 'Jen', 'Sarah', 'Adam']

print(friends[:2])  
# From start to index 1: ['Rolf', 'Bob']

print(friends[:])  
# Full copy of the list

print(friends[0:3:2])  
# From index 0 to 2 with step 2: ['Rolf', 'Anne']

print(friends[::2])  
# Every second element: ['Rolf', 'Anne', 'Jen', 'Adam']

print(friends[::])  
# Full list (same as friends[:])

print(friends[1:3])  
# From index 1 to 2: ['Bob', 'Anne']

print(friends[1:3][0])  
# First element of sliced list ['Bob', 'Anne'] → Bob

print(friends[1:3][1])  
# Second element of sliced list ['Bob', 'Anne'] → Anne

# print(friends[1:3][2])  
# Error: Index out of range (only 2 items in slice)


print("-------------list Functions-----------------")

# Add "Rolf" to the end of the list
friends.append("Rolf")
print(friends)

# Add another "Rolf" to the end of the list
friends.append("Rolf")
print(friends)

# Insert "Ahmed" at index 0 (beginning of the list)
friends.insert(0, "Ahmed")
print(friends)

# Insert "Sophie" at index 3
friends.insert(3, "Sophie")
print(friends)

# Remove the first occurrence of "Sophie" from the list
friends.remove("Sophie")
print(friends)

# Remove the last item from the list
friends.pop()
print(friends)

# Remove all items from the list (clear it completely)
# friends.clear()
# print(friends)

# Find the index (position) of "Rolf" in the friends list
# print(friends.index("Rolf"))


# Count how many times "Rolf" appears in the friends list
print(friends.count("Rolf"))


# Sort the friends list in ascending (alphabetical) order
# NOTE: sort() changes the list in place and returns None, so printing it shows None
print(friends.sort())


# List of lucky numbers
lucky_numbers = [4, 8, 15, 16, 23, 42]

# Sort the numbers in ascending order
lucky_numbers.sort()

# Print the sorted list
print(lucky_numbers)

# Reverse the order of the list (last item becomes first, first becomes last)
lucky_numbers.reverse()

# Print the reversed list
print(lucky_numbers)



# Create a copy of the friends list (a new separate list with same elements)
print(friends.copy())


#remove duplicates from a list using set
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
print(unique)