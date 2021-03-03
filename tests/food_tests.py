import unittest
# from src.customer import Customer
from src.food import Food
# from src.pub import Pub

class TestFood (unittest.TestCase):
    def setUp(self):
        self.food_1 = Food("Chips", 10.0, 5)
        self.food_2 = Food("Chicken Nuggets", 12.5, 8)

    def test_food_has_name(self):
        self.assertEqual("Chips", self.food_1.name)

    def test_food_has_price(self):
        self.assertEqual(10.0, self.food_1.price)

    def test_food_has_rejuvenation_level(self):
        self.assertEqual(5, self.food_1.rejuvenation_level)    