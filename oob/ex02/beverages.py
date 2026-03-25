class HotBeverage:
    name: str = 'hot beverage'
    price: float = 0.30
    desc: str = 'Just some hot water in a cup.'

    def description(self):
        return self.desc

    def __str__(self):
        return f'name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}'

class Coffee(HotBeverage):
    name = 'coffee'
    price = 0.40
    desc = 'A coffee, to stay awake.'

class Tea(HotBeverage):
    name = 'tea'

class Chocolate(HotBeverage):
    name = 'chocolate'
    price = 0.50
    desc = 'Chocolate, sweet chocolate...'

class Cappuccino(HotBeverage):
    name = 'cappuccino'
    price = 0.45
    desc = 'Un po´ di Italia nella sua tazza!'