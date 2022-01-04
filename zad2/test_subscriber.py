from unittest import TestCase
from unittest.mock import *
from zad2.subscriber import Subscriber


class SubscriberTest(TestCase):
    def setUp(self):
        self.temp = Subscriber()

    def test_add_client1(self):
        self.temp.add_client=MagicMock(return_value=["Wojtek"])
        self.assertEqual(self.temp.add_client("Wojtek"),["Wojtek"])

    def test_add_client2(self):
        self.temp.clients=["Wojtek","Sebastian"]
        self.temp.add_client=MagicMock(return_value=["Wojtek","Sebastian","Adam"])
        self.assertEqual(self.temp.add_client("Adam"),["Wojtek","Sebastian","Adam"])

    def test_add_client_error1(self):
        self.temp.add_client=MagicMock(side_effect=ValueError)
        with self.assertRaises(ValueError):
            self.temp.add_client(["Wojtek"])

    def test_add_client_error2(self):
        self.temp.add_client=MagicMock(side_effect=ValueError)
        with self.assertRaises(ValueError):
            self.temp.add_client(123)

    def test_delete_client1(self):
        self.temp.clients=["Wojtek","Sebastian"]
        self.temp.delete_client=MagicMock(return_value=["Wojtek"])
        self.assertEqual(self.temp.delete_client("Sebastian"),["Wojtek"])

    def test_delete_client2(self):
        self.temp.clients=["Wojtek","Sebastian"]
        self.temp.delete_client=MagicMock(return_value=["Sebastian"])
        self.assertEqual(self.temp.delete_client("Wojtek"),["Sebastian"])

    def test_delete_client_error1(self):
        self.temp.delete_client=MagicMock(side_effect=ValueError)
        with self.assertRaises(ValueError):
            self.temp.delete_client(["Wojtek"])

    def test_delete_client_error_empty(self):
        self.temp.delete_client=MagicMock(side_effect=ValueError)
        with self.assertRaises(ValueError):
            self.temp.delete_client("Adam")

    def test_message_client1(self):
        self.temp.send_message_client=MagicMock(return_value=True)
        self.assertTrue(self.temp.send_message_client("Wojtek","hi"))

    def test_message_client_error1(self):
        self.temp.send_message_client=MagicMock(side_effect=ValueError)
        with self.assertRaises(ValueError):
            self.temp.send_message_client(["Wojtek"],"hello")

    def test_message_client_error2(self):
        self.temp.send_message_client=MagicMock(side_effect=ValueError)
        with self.assertRaises(ValueError):
            self.temp.send_message_client("Wojtek",["hello"])

    def test_message_client_error3_nouser(self):
        self.temp.send_message_client=MagicMock(side_effect=ValueError)
        with self.assertRaises(ValueError):
            self.temp.send_message_client("Wojtek","hello")