from beverages import HotBeverage
from random import randint

class CoffeeMachine:

    def __init__(self):
        self.servings_count = 0

    class EmptyCup(HotBeverage):
        name = 'empty cup'
        price = 0.90
        desc = 'An empty cup!? Gimme my money back!'

    class BrokenMachineException(Exception):
        def __init__(self):
            self.message = 'This coffee machine has to be repaired.'

    def serve(self, beverage: HotBeverage):
        if (self.servings_count == 10):
            raise self.BrokenMachineException()
        else:
            self.servings_count += 1
            return self.EmptyCup() if randint(0,1) == 0 else beverage()

    def repair(self):
        self.servings_count = 0