from main import get_weather
import pytest

def test_get_weather():
    assert get_weather(-5) == "Freezing"
    assert get_weather(5) == "Cold"
    assert get_weather(15) == "Cool"
    assert get_weather(25) == "Warm"


def test_add():
    from main import add
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_divide():
    from main import divide
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)



from main import UserManager
@pytest.fixture
def user_manager():
    """ Create a fresh instance of UserManager for each test """
    return UserManager()


def test_user_manager(user_manager):
    assert user_manager.add_user("john_doe", "john@example.com") == True
    assert user_manager.get_user("john_doe") == "john@example.com"

def test_add_user_duplicate(user_manager):
    user_manager.add_user("john_doe", "john@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("john_doe", "another@example.com")


from main import is_prime
@pytest.mark.parametrize("num, expected", [
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (10, False),
    (13, True),
    (1, False),
    (0, False),
    (-5, False)
])

def test_is_prime(num, expected):
    assert is_prime(7) == True
    assert is_prime(num) == expected


from main import get_weather
def test_get_weather_api(mocker):
    mock_get = mocker.patch('main.requests.get')

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temp": 25, "condition": "Sunny"}
    
    result = get_weather("New York")

    assert result == {"temp": 25, "condition": "Sunny"}
    mock_get.assert_called_once_with("https://api.weather.com//v1/New York")
    