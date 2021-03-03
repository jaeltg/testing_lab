import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub
from src.food import Food

class TestPub (unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Mojito", 8.0, 7)
        self.drink_2 = Drink("Pilsen", 6.5, 4)

        self.customer_1 = Customer("Malcolm", 25.0, 28)
        self.customer_2 = Customer("Erika", 30.0, 17)

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

    def test_can_find_drink_by_name(self):
        self.pub.find_drink_by_name(self.drink_1)
        self.assertEqual("Mojito", self.drink_1.name)

    def test_can_check_customer_age__overage(self):
        self.assertEqual(False, self.pub.check_if_under_age(self.customer_1))

    def test_can_check_customer_age__underage(self):
        self.assertEqual(True, self.pub.check_if_under_age(self.customer_2))        
        
    def test_can_check_customer_drunkennes__drunk(self):
        self.pub.sell_drink(self.drink_1, self.customer_1)
        self.pub.sell_drink(self.drink_2, self.customer_1)
        self.assertEqual(True, self.pub.check_if_drunk(self.customer_1))

    def test_can_check_customer_drunkennes__not_drunk(self):
        self.pub.sell_drink(self.drink_1, self.customer_1)
        self.assertEqual(False, self.pub.check_if_drunk(self.customer_1))    

    def test_pub_sell_drink(self):
        self.pub.sell_drink(self.drink_2, self.customer_1)
        self.assertEqual(18.5, self.customer_1.wallet)
        self.assertEqual(506.5, self.pub.till)
        self.assertEqual(1, self.customer_1.drink_count())
        self.assertEqual(4, self.customer_1.drunkenness_level)    

  
