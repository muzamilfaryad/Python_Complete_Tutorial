# ----------------------------
# SETS IN PYTHON (BASICS)
# ----------------------------

# A set is an unordered collection of unique elements
# It does NOT allow duplicate values
# It is mutable (you can add/remove items)
# It is written using curly braces {}

my_set = {1, 2, 3, 4, 5}

# Print initial set
print("Original set:", my_set)

# ----------------------------
# ADD ELEMENT
# ----------------------------
# add() → adds a single element to the set
my_set.add(6)
print("After adding 6:", my_set)

# ----------------------------
# REMOVE ELEMENT
# ----------------------------
# remove() → removes an element
# BUT raises error if element is not found
my_set.remove(3)
print("After removing 3:", my_set)

# ----------------------------
# ADD DUPLICATE VALUE
# ----------------------------
# Sets do NOT allow duplicates
# So adding 2 again will NOT change the set
my_set.add(2)
print("After adding duplicate 2:", my_set)

# ----------------------------
# DISCARD ELEMENT
# ----------------------------
# discard() → removes element if exists
# DOES NOT raise error if element is missing
my_set.discard(10)  # 10 is not in set, but no error
print("After discarding 10 (not present):", my_set)

# ----------------------------
# CLEAR SET
# ----------------------------
# clear() → removes all elements from set
my_set.clear()
print("After clearing set:", my_set)


# ----------------------------
# EXTRA SET CONCEPTS (IMPORTANT)
# ----------------------------

A = {1, 2, 3}
B = {3, 4, 5}

# Union → combines both sets (no duplicates)
print("Union:", A.union(B))

# Intersection → common elements
print("Intersection:", A.intersection(B))

# Difference → elements in A but not in B
print("Difference (A - B):", A.difference(B))

# Symmetric Difference → elements not common in both
print("Symmetric Difference:", A.symmetric_difference(B))