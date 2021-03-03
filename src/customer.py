class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.drinks = []
        
    def reduce_money(self, amount):
        self.wallet -= amount

    def add_drink(self, drink):
        self.drinks.append(drink)    

    def drink_count(self):
        return len(self.drinks) 

    # def buy_drink(self, drink, pub):
    #     drink = pub.find_drink_by_name(drink)
    #     if drink.price > self.wallet:
    #         return
    #     self.reduce_money(drink.price)
    #     pub.increase_till(drink.price)
    #     self.add_drink(drink)