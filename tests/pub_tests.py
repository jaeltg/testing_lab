import unittest
# from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestPub (unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Mojito", 8.0)
        self.drink_2 = Drink("Pilsen", 6.5)

        drinks = [self.drink_1, self.drink_2]
        self.pub = Pub("JP's", drinks, 500)

    def test_pub_has_name(self):
        self.assertEqual("JP's", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(500, self.pub.till)    

    def test_pub_has_drinks(self):
        self.assertEqual(2, self.pub.drink_count())