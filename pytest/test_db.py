import pytest
from db import Database

@pytest.fixture
def db():
    """ Provide a fresh instance of Database for each test """
    return Database() #Provide the fixture with a fresh instance of Database for each test
    database.data.clear()  # Clear data before each test

def test_add_user(db):
    db.add_user(1, "Alice")
    assert db.get_user(1) == "Alice"

def test_add_user_duplicate(db):    
    db.add_user(1, "Alice")
    with pytest.raises(ValueError, match="User ID already exists"):
        db.add_user(1, "Bob")

def test_delete_user(db):
    db.add_user(1, "Alice")
    db.delete_user(1)
    assert db.get_user(1) is None

from db import save_user_to_db
def test_save_user_to_db(mocker):
    mock_conn = mocker.patch('db.sqlite3.connect')
    mock_cursor = mock_conn.return_value.cursor.return_value

    save_user_to_db("Alice", 30)

    mock_conn.assert_called_once_with('users.db')

    mock_cursor.execute.assert_called_once_with(
        '''INSERT INTO users (name, age) VALUES (?, ?)''',
        ("Alice", 30)
    )

    mock_conn.return_value.commit.assert_called_once()
    mock_conn.return_value.close.assert_called_once()