class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.drinks = []
        self.age = age
        self.drunkenness_level = 0
        
    def reduce_money(self, amount):
        self.wallet -= amount

    def add_drink(self, drink):
        self.drinks.append(drink)    

    def drink_count(self):
        return len(self.drinks) 

    def increase_drunkennes(self, drink):
        self.drunkenness_level += drink.alcohol_level
