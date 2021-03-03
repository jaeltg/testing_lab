class Pub:
    def __init__(self, name, drinks, till):
        self.name = name
        self.drinks = drinks
        self.till = till

    def drink_count(self):
        return len(self.drinks)    