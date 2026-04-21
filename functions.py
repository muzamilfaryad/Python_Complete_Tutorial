

def sayhi():
    print("Hi User!")

sayhi()


def say_hi():
    print("Hi User!")

say_hi()


#parameters
def say_hi(name):
    print(f"Hi {name}!")
say_hi("Alice")
def say_hi(name, age):
    print(f"Hi {name}, you are {age} years old!")
say_hi("Bob", 30)
#return values



def hello(name , age , serial_number):
    print("Hello, " + name + "! You are " + str(age) + " years old. Your serial number is " + serial_number + ".")

hello("Charlie", 25, "SN123")



print("----------Return Statement----------")

def add(a, b):
    return a + b
result = add(5, 3)
print(result)  # Output: 8


def cube(num):
    return num ** 3
print(cube(2))  # Output: 8
