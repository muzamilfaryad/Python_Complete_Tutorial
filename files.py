# # Open the file in read mode ("r")
# employee_file = open("employees.txt", "r")

# # Check if the file is readable (returns True or False)
# print(employee_file.readable())

# # Always close the file after use to free resources
# employee_file.close()


# # Open the file in write mode ("w")
# # This will overwrite the file if it already exists
# employee_file = open("employees.txt", "w")

# # Check if the file is writable
# print(employee_file.writeable())

# # Close the file
# employee_file.close()


# # Open the file in append mode ("a")
# # This will add new content to the end of the file
# employee_file = open("employees.txt", "a")

# # Check if the file is writable (append mode allows writing)
# print(employee_file.writeable())

# # Close the file
# employee_file.close()


# # Open the file in read and write mode ("r+")
# # Allows both reading and writing without overwriting the file
# employee_file = open("employees.txt", "r+")

# # Check if the file is writable
# print(employee_file.writeable())

# # Close the file
# employee_file.close()



employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()

employee_file = open("employees.txt", "r")
print(employee_file.readline())
print(employee_file.readline())
employee_file.close()


employee_file = open("employees.txt", "r")
print(employee_file.readlines())
employee_file.close()


employee_file = open("employees.txt", "r")
print(employee_file.readlines()[1])
employee_file.close()


employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()



#Writing Files

employee_file = open("employees.txt", "a")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

employee_file = open("employees.txt", "a")
employee_file.write("\nKally - Customer Service")
employee_file.close()


employee_file = open("employees.txt", "w")
employee_file.write("\nKally - Customer")
employee_file.close()

employee_file = open("employees1.txt", "w")
employee_file.write("\nKally - Customer")
employee_file.close()

employee_file = open("employees.txt", "w")
employee_file.write("<p>This is a new line of text</p>")
employee_file.close()