

def get_weather(temperature):
    if temperature < 0:
        return "Freezing"
    elif 0 <= temperature < 10:
        return "Cold"
    elif 10 <= temperature < 20:
        return "Cool"
    elif 20 <= temperature < 30:
        return "Warm"
    else:
        return "Hot"


def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b



class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email):
        if username in self.users:
            raise ValueError("Username already exists")
        self.users[username] = email
        return True

    def get_user(self, username):
        return self.users.get(username)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


import requests
def get_weather(city):
    response = requests.get(f"https://api.weather.com//v1/{city}")
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("City not found")