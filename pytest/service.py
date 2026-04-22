import requests
class APIClient:
    """ Simulates an external API client """
    def get_user_data(self, user_id):
        response = requests.get(f"https://api.example.com/users/{user_id}")
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError("User not found") 

class UserService:
    """ Service that uses APIClient to fetch and process user data """
    def __init__(self, api_client):
        self.api_client = api_client

    def get_username(self, user_id):
        user_data = self.api_client.get_user_data(user_id)
        return user_data["name"].upper() # Process the name to uppercase