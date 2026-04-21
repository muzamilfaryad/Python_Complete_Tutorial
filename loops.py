# -------------------------------
# WHILE LOOP
# -------------------------------

# Initialize variable
i = 1

# Loop runs while condition is True
while i <= 5:
    print(i)        # Print current value of i
    i += 1          # Increment i by 1

# This runs after the loop ends
print("Done")


# -------------------------------
# FOR LOOP (String iteration)
# -------------------------------

# Loop through each character in the string
for letter in "Giraffe Academy":
    print(letter)


# -------------------------------
# FOR LOOP (List iteration)
# -------------------------------

# List of friends
friends = ["Jim", "Karen", "Kevin"]

# Loop through each item in the list
for friend in friends:
    print(friend)


# -------------------------------
# FOR LOOP with range()
# -------------------------------

# Loop from 0 to 9 (10 values)
for index in range(10):
    print(index)

# Loop from 3 to 9
for index in range(3, 10):
    print(index)


# -------------------------------
# FOR LOOP using index (len)
# -------------------------------

# List of friends
friends = ["Jim", "Karen", "Kevin"]

# Loop using index values
for index in range(len(friends)):
    print(friends[index])   # Access elements using index


# -------------------------------
# FOR LOOP with if-else
# -------------------------------

# Loop from 0 to 4
for index in range(5):
    if index == 0:
        print("First Iteration")   # Runs only for first loop
    else:
        print("Other Iteration")   # Runs for remaining loops


# -------------------------------
# 2D Loops and Nested Loops
# -------------------------------

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])  # Output: 1


for row in number_grid:          # Outer loop iterates through each row
    for col in row:             # Inner loop iterates through each column in the current row
        print(col)              # Print the current element