import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer (unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Malcolm", 25.0)
        self.drink = Drink("Pilsen", 6.5)

    def test_customer_has_name(self):
        self.assertEqual("Malcolm", self.customer.name)   

    def test_customer_has_wallet(self):
        self.assertEqual(25.0, self.customer.wallet) 

    def test_reduce_money_in_wallet(self):
        self.customer.reduce_money(6.5)
        self.assertEqual(18.5, self.customer.wallet)