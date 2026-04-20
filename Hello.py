print("Hello from VS Code")
print("............./")
print("............/")
print(".........../")
print("........../")

# Variables
#string
name = "John"
#number
age = 30
print("My name is " + name + " and I am " + str(age) + " years old.")

name = "Tom"
age = 25
print("My name is " + name + " and I am " + str(age) + " years old.")

#bolean
is_student = True
print("Is student: " + str(is_student))

#next line
print("This is the first line.\nThis is the next line.")

print("------------------------Working With Strings------------------------")


#concatination
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)

#lower()
phase = "Python"
print("phase.lower(): " + phase.lower())

#uppper()
phase = "Python"
print("phase.upper(): " + phase.upper())

#uppper(),bolean
phase = "Python"
print("phase.upper(): " , phase.upper().isupper())

#len()
phrase = "Python"
print("len(phrase): " + str(len(phrase)))

#individual characters
phrase = "Python"
print("phrase[0]: " + phrase[0])
print("phrase[1]: " + phrase[1])
print("phrase[2]: " + phrase[2])
print("phrase[3]: " + phrase[3])
print("phrase[4]: " + phrase[4])
print("phrase[5]: " + phrase[5])

#index_function
phrase = "Python"
print("phrase.index('y'): " + str(phrase.index('y')))

#replace()
phrase = "Python"
print("phrase.replace('o', 'a'): " + phrase.replace('o', 'a'))



print("------------------------Working With Numbers------------------------")

number = 10
print(number) 
print("number + 5: " + str(number + 5))

print("5 + 3: " + str(5 + 3))
print("5 - 3: " + str(5 - 3))
print("5 * 3: " + str(5 * 3))
print("5 / 3: " + str(5 / 3))
print("5 // 3: " + str(5 // 3))
print("5 % 3: " + str(5 % 3))
print("5 ** 3: " + str(5 ** 3))


#absoluute_value
abs_value = abs(-5)
print("abs_value: " + str(abs_value))

#power
power_value = pow(3, 2)
print("power_value: " + str(power_value))


#max
max_value = max(5, 10)
print("max_value: " + str(max_value))

#min
min_value = min(5, 10)
print("min_value: " + str(min_value))

#round
rounded_value = round(3.14159, 2)
print("rounded_value: " + str(rounded_value))


print("------------------------Some Math Functions------------------------")

from math import *
print("math.sqrt(16): " + str(sqrt(16)))
print("math.ceil(3.2): " + str(ceil(3.2)))
print("math.floor(3.7): " + str(floor(3.7)))
print("math.pi: " + str(pi))


print("------------------------Getting User Input------------------------")

input_name = input("Enter your name: ")
print("Hello, " + input_name + "!")

age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")