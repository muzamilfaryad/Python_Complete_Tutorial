# =========================
# IF STATEMENTS PRACTICE
# =========================

# -------------------------
# 1. Simple if statement
# -------------------------
age = 18

if age >= 18:
    print("You are an adult.")  # Runs only if condition is True


# -------------------------
# 2. if-else statement
# -------------------------
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")  # Runs when condition is False


# -------------------------
# 3. if-elif-else statement
# -------------------------
age = 70

if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")  # Runs when all above conditions fail


# -------------------------
# 4. Nested if statement
# -------------------------
age = 25

if age >= 18:
    # First condition is True, now checking inside it
    if age < 65:
        print("You are an adult.")
    else:
        print("You are a senior.")
else:
    print("You are a minor.")


# -------------------------
# 5. Logical operators (and / or)
# -------------------------
age = 30

# AND: both conditions must be True
if age >= 18 and age < 65:
    print("You are an adult.")

# OR: at least one condition must be True
if age < 18 or age >= 65:
    print("You are not an adult.")


# -------------------------
# 6. Boolean example
# -------------------------
# Boolean means True or False

is_male = True  # Change to True to test
is_tall = True
#or , and , not are used to combine boolean values
if is_male or is_tall:
    print("You are a male or tall or both.")
elif is_male and not is_tall:
    print("You are a male but not tall.")
elif not is_male and is_tall:
    print("You are not a male but tall.")
else:
    print("You are neither a male nor tall.")

# If Statements and Comparison Operators

# Comparison operators: ==, !=, >, <, >=, <=

# Example: Check if a number is positive, negative, or zero
number = -5
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



  # Function to find the maximum of three numbers
def max_number(num1, num2, num3):
    # Check if num1 is the greatest
    if num1 >= num2 and num1 >= num3:
        return num1

    # Check if num2 is the greatest
    elif num2 >= num1 and num2 >= num3:
        return num2

    # Otherwise num3 is the greatest
    else:
        return num3


# Example: Find the maximum of three numbers
num1 = 10
num2 = 20
num3 = 15

# Call the function correctly
max_num = max_number(num1, num2, num3)

# Print the result
print("The maximum number is:", max_num)



# Simple Calculator Program

# Take first number as input and convert it to float
num1 = float(input("Enter the first number: "))

# Take operator input (+, -, *, /)
op = input("Enter an operator (+, -, *, /): ")

# Take second number as input and convert it to float
num2 = float(input("Enter the second number: "))

# Perform addition
if op == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

# Perform subtraction
elif op == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

# Perform multiplication
elif op == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

# Perform division with zero check
elif op == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

# Handle invalid operator input
else:
    print("Invalid operator! Please use +, -, *, or /")