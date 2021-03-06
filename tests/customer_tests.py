import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub
from src.food import Food

class TestCustomer (unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Malcolm", 25.0, 28)
        self.drink_1 = Drink("Mojito", 8.0, 7)
        self.drink_2 = Drink("Pilsen", 6.5, 4)
        self.food_1 = Food("Chips", 10.0, 5)
        self.food_2 = Food("Chicken Nuggets", 12.5, 8)

        drinks = [self.drink_2, self.drink_1]
        self.pub = Pub("JP's", drinks, 500)

    def test_customer_has_name(self):
        self.assertEqual("Malcolm", self.customer.name) 

    def test_customer_has_age(self):
        self.assertEqual(28, self.customer.age)    

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

    def test_can_increase_drunkennes(self):
        self.customer.increase_drunkennes(self.drink_1)
        self.assertEqual(7, self.customer.drunkenness_level)   

    def test_can_decrease_drunkennes(self):
        self.customer.increase_drunkennes(self.drink_1)
        self.customer.decrease_drunkennes(self.food_1)
        self.assertEqual(2, self.customer.drunkenness_level)     
   

