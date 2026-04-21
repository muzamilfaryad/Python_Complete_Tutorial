"""
COMMENTS IN PYTHON - A Comprehensive Guide

Comments are lines of text in your code that are NOT executed by Python.
They are used to explain what your code does, making it easier for you and others to understand.
"""

# ============================================================================
# 1. SINGLE-LINE COMMENTS
# ============================================================================
# A single-line comment starts with a hash symbol (#)
# Everything after # on that line is ignored by Python

# This is a comment
print("Hello, World!")  # This is also a comment (inline comment)

# Comments are useful for explaining complex logic
age = 25  # Store the user's age
if age >= 18:  # Check if person is an adult
    print("You are an adult")


# ============================================================================
# 2. MULTI-LINE COMMENTS
# ============================================================================
# For longer explanations, you can use multiple single-line comments
# Just add a # symbol at the beginning of each line
# This is still a comment
# And this too
# Comments can span as many lines as you need

# Example: Multi-line comment explaining a calculation
# We calculate the area of a rectangle by multiplying
# the length by the width. This is useful for finding
# how much space something takes up.
length = 10
width = 5
area = length * width
print(f"Area of rectangle: {area}")


# ============================================================================
# 3. DOCSTRINGS (Triple Quotes)
# ============================================================================
"""
Docstrings are a special type of comment used to document functions, classes, and modules.
They use triple quotes (either """ or ''') and appear right after the definition.
Docstrings are different from regular comments - they're actually part of the code
and can be accessed using the help() function.
"""

def greet(name):
    """
    This is a docstring. It describes what the function does.
    
    Args:
        name (str): The name of the person to greet
    
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"

# Access the docstring with help()
help(greet)


# ============================================================================
# 4. WHEN TO USE COMMENTS
# ============================================================================

# ✓ GOOD: Explain WHY, not WHAT
# We multiply by 0.05 because sales tax is 5%
tax = total_price * 0.05

# ✗ BAD: Obvious what the code does
# Multiply x by 2
result = x * 2

# ✓ GOOD: Explain complex logic
# Using binary search for efficiency on large datasets
def search_algorithm(data, target):
    # Implementation here
    pass

# ✓ GOOD: Document assumptions
# Assuming user input is always a positive integer
def calculate_factorial(n):
    pass

# ✓ GOOD: Mark important sections
# TODO: Need to fix this bug when database is ready
# FIXME: This calculation is incorrect
# HACK: Temporary solution - refactor later
# NOTE: This function is deprecated - use new_function() instead


# ============================================================================
# 5. COMMENTED-OUT CODE
# ============================================================================
# Sometimes you might comment out code while testing
# print("This code won't run")
# x = 10
# y = 20

# But it's better to use version control (Git) instead of leaving
# commented code in production - it makes the code messy!


# ============================================================================
# 6. PRACTICAL EXAMPLES
# ============================================================================

# Example 1: Simple calculator with comments
def add(a, b):
    """Returns the sum of two numbers"""
    return a + b

def multiply(a, b):
    """Returns the product of two numbers"""
    return a * b

# Get user inputs
# (In a real app, add error handling)
num1 = 10
num2 = 5

# Calculate and display results
sum_result = add(num1, num2)
product = multiply(num1, num2)
print(f"Sum: {sum_result}")
print(f"Product: {product}")


# Example 2: Loop with comments explaining the logic
# Iterate through numbers 1 to 5
for i in range(1, 6):
    # Print each number
    print(f"Number: {i}")
    
    # Check if the number is even
    if i % 2 == 0:
        print(f"  {i} is even")
    else:
        # Number is odd
        print(f"  {i} is odd")


# ============================================================================
# SUMMARY: COMMENT BEST PRACTICES
# ============================================================================
"""
1. Write clear, concise comments
2. Explain WHY, not WHAT
3. Keep comments up-to-date with code changes
4. Don't overuse comments - write readable code
5. Use docstrings for functions and classes
6. Use meaningful variable names to reduce comment needs
7. Avoid obvious comments ("x = 5  # Set x to 5")
8. Use comments to explain edge cases and assumptions
"""
