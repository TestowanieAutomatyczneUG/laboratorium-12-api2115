from unittest import TestCase
from unittest.mock import *
from zad1.user import User
import json

def load_data():
    with open("data", "r") as f:
        return json.loads(f.read())

class TestUser(TestCase):
    def setUp(self):
        self.temp=User()

    def test_get_data(self):
        self.temp.get_data=MagicMock(return_value=load_data())
        self.assertEqual(self.temp.get_data(),load_data())

    def test_get_email(self):
        self.temp.get_data = MagicMock(return_value=load_data())
        self.assertEqual(self.temp.get_email(),"brad.gibson@example.com")

    def test_get_full_name(self):
        self.temp.get_data = MagicMock(return_value=load_data())
        self.assertEqual(self.temp.get_full_name(),"mr brad gibson")

    def tearDown(self):
        self.temp=None