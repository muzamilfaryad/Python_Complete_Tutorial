

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



#Exponential function
def power(base, exponent):
    return base ** exponent
print(power(2, 3))  # Output: 8


def raise_to_power(base, pow):
    result = 1
    for i in range(pow):
        result *= base
    return result
print(raise_to_power(2, 3))  # Output: 8


print("---------Type Hints----------")

#Type hints are a way to indicate the expected data types of function parameters and return values. 
#They are not enforced by Python but can help with code readability and static analysis.
def greet(name: str) -> str:
    return f"Hello, {name}!"
print(greet("Dave"))  # Output: Hello, Dave!

# Explanation:
# name: str → input should be a string
# -> str → function returns a string


# Type hints are annotations that show expected data types of variables, function parameters, and return values.

# They help:

# Improve code readability
# Help IDEs (autocomplete, warnings)
# Enable static analysis tools like mypy

# ⚠️ Python does NOT enforce them at runtime.


# Type Hints for Variables
age: int = 25
name: str = "Ali"
height: float = 5.9
is_student: bool = True

# Multiple Parameters
def add(a: int, b: int) -> int:
    return a + b

# Common Built-in Types
# Type	Example
# int	10
# float	3.14
# str	"hello"
# bool	True
# list	[1, 2, 3]
# dict	{"a": 1}

# Lists with Type Hints
# from typing import List
def process_numbers(nums: List[int]) -> int:
    return sum(nums)

# Modern Python (3.9+):
def process_numbers(nums: list[int]) -> int:
    return sum(nums)

# Dictionaries
# from typing import Dict
def user_data(data: Dict[str, int]) -> None:
    print(data)

# Modern:
def user_data(data: dict[str, int]) -> None:
    print(data)

# Optional Types
# Used when value can be None.

from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Ali"
    return None

# Modern:

def find_user(user_id: int) -> str | None:
    return None

# 9. Union Types (Multiple possible types)
from typing import Union

def process(value: Union[int, str]):
    print(value)

# Modern:

def process(value: int | str):
    print(value)

# 10. Any Type (No restriction)
from typing import Any

def handle(data: Any):
    print(data)

# 11. Tuples
from typing import Tuple

def coordinates() -> Tuple[int, int]:
    return (10, 20)

# Modern:

def coordinates() -> tuple[int, int]:
    return (10, 20)

# 12. Type Aliases (Custom Types)
from typing import List

Numbers = list[int]

def square(nums: Numbers) -> list[int]:
    return [n * n for n in nums]

# 13. Function Type (Callable)
from typing import Callable

def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

# 14. Why Type Hints Matter (Real Benefits)

# Easier debugging
# Cleaner code structure
# Better collaboration
# Helps large projects scale
# Used in AI/ML, Django, FastAPI, etc.

# 15. Your Example (Enhanced)
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Dave"))

# Summary

# Type hints are:

# Optional
# For readability
# For tools (not runtime enforcement)