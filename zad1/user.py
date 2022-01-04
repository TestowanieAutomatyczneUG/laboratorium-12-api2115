import requests

class User:
    def __init__(self):
        self.data = None

    def get_data(self):
        data = requests.get("https://randomuser.me/api/").json()
        self.data = data
        return data

    def get_email(self):
        return self.get_data().get("results")[0].get("email")

    def get_full_name(self):
        user_info = self.get_data().get("results")[0].get("name")
        return user_info.get("title")+" "+user_info.get("first")+" "+user_info.get("last")
