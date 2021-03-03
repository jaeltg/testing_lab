import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestPub (unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Mojito", 8.0)
        self.drink_2 = Drink("Pilsen", 6.5)

        self.customer = Customer("Malcolm", 25.0)

        drinks = [self.drink_2, self.drink_1]
        self.pub = Pub("JP's", drinks, 500)

    def test_pub_has_name(self):
        self.assertEqual("JP's", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(500, self.pub.till)    

    def test_pub_has_drinks(self):
        self.assertEqual(2, self.pub.drink_count())

    def test_can_increase_till(self):
        self.pub.increase_till(8.0)
        self.assertEqual(508.0, self.pub.till)   

    def test_pub_sell_drink(self):
        self.pub.sell_drink(self.drink_2, self.customer)
        self.assertEqual(18.5, self.customer.wallet)
        self.assertEqual(506.5, self.pub.till)
        self.assertEqual(1, self.customer.drink_count())     