from zad1.user import User
from unittest import TestCase

class TestUser(TestCase):
    def setUp(self):
        self.temp=User()

    def test_get_data1(self):
        self.assertEqual(len(self.temp.get_data()),2)

    def test_get_data2(self):
        self.assertEqual(type(self.temp.get_data()),dict)

    def test_get_email(self):
        self.assertEqual(type(self.temp.get_email()), str)

    def test_get_full_name1(self):
        self.assertEqual(type(self.temp.get_full_name()), str)

    def test_get_full_name2(self):
        self.assertEqual(self.temp.get_full_name()[0], "M")

    def tearDown(self):
        self.temp=None