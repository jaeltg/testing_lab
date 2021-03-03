import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer (unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Malcolm", 25.0)
        self.drink_1 = Drink("Mojito", 8.0)
        self.drink_2 = Drink("Pilsen", 6.5)

        drinks = [self.drink_2, self.drink_1]
        self.pub = Pub("JP's", drinks, 500)

    def test_customer_has_name(self):
        self.assertEqual("Malcolm", self.customer.name)   

    def test_customer_has_wallet(self):
        self.assertEqual(25.0, self.customer.wallet) 

    def test_reduce_money_in_wallet(self):
        self.customer.reduce_money(6.5)
        self.assertEqual(18.5, self.customer.wallet)

    def test_drink_list_is_empty(self):
         self.assertEqual(0, self.customer.drink_count())   

    def test_add_drink(self):
        self.customer.add_drink(self.drink_1)
        self.assertEqual(1, self.customer.drink_count())  
   
    # def test_customer_buys_drink(self):
    #     self.customer.buy_drink(self.drink_2, self.pub)
    #     self.assertEqual(18.5, self.customer.wallet)
    #     self.assertEqual(506.5, self.pub.till)
    #     self.assertEqual(1, self.customer.drink_count())
