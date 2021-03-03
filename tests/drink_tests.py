import unittest
# from src.customer import Customer
from src.drink import Drink
# from src.pub import Pub

class TestDrink (unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Mojito", 8.0)
        self.drink_2 = Drink("Pilsen", 6.5)

    def test_drink_has_name(self):
        self.assertEqual("Mojito", self.drink_1.name)

    def test_drink_has_price(self):
        self.assertEqual(8.0, self.drink_1.price)