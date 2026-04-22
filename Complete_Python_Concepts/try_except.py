# First example: basic exception handling

try:
    # This line will cause a ZeroDivisionError (cannot divide by zero)
    value = 10 / 0
    
    # Taking user input and converting it to integer
    number = int(input("Enter a number: "))
    
    # Printing the entered number
    print(number)

# Handles division by zero error
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Handles invalid input (e.g., if user enters text instead of number)
except ValueError:
    print("Invalid input! Please enter a valid number.")


# Second example: exception handling with error details

try:
    # This will again raise a ZeroDivisionError
    value = 10 / 0
    
    # Taking user input and converting it to integer
    number = int(input("Enter a number: "))
    
    # Printing the entered number
    print(number)

# Captures the error object as 'err' and prints detailed message
except ZeroDivisionError as err:
    print(f"Error: Division by zero is not allowed. Details: {err}")

# Captures ValueError and prints detailed message
except ValueError as err:
    print(f"Invalid input! Please enter a valid number. Details: {err}")