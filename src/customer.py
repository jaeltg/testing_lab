class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        
    def reduce_money(self, amount):
        self.wallet -= amount
