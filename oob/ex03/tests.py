from machine import CoffeeMachine
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

def main():
    # Create coffee machine
    machine = CoffeeMachine()

    # Serve 10 drinks and try to serve the 11th
    drink = machine.serve(Cappuccino)
    print(f' - 1st drink:\n{drink.__str__()}\n')
    drink = machine.serve(Coffee)
    print(f' - 2nd drink:\n{drink.__str__()}\n')
    drink = machine.serve(Chocolate)
    print(f' - 3rd drink:\n{drink.__str__()}\n')
    drink = machine.serve(Tea)
    print(f' - 4th drink:\n{drink.__str__()}\n')
    drink = machine.serve(HotBeverage)
    print(f' - 5th drink:\n{drink.__str__()}\n')
    drink = machine.serve(Cappuccino)
    print(f' - 6th drink:\n{drink.__str__()}\n')
    drink = machine.serve(Coffee)
    print(f' - 7th drink:\n{drink.__str__()}\n')
    drink = machine.serve(Chocolate)
    print(f' - 8th drink:\n{drink.__str__()}\n')
    drink = machine.serve(Tea)
    print(f' - 9th drink:\n{drink.__str__()}\n')
    drink = machine.serve(HotBeverage)
    print(f' - 10th drink:\n{drink.__str__()}\n')
    try:
        drink = machine.serve(Coffee)
    except CoffeeMachine.BrokenMachineException as e:
        print(f'Exception: {e.message}')

    # Try again
    try:
        drink = machine.serve(Coffee)
    except CoffeeMachine.BrokenMachineException as e:
        print(f'Exception: {e.message}')

    # Repair the machine and then try again
    machine.repair()
    drink = machine.serve(Coffee)
    print(f' - 11th drink:\n{drink.__str__()}\n')

    # Let's break it again...
    try:
        for i in range (2,12):
            drink = machine.serve(Chocolate)
            print(f'- Drink number {i} after repair:\n{drink.__str__()}\n')
    except CoffeeMachine.BrokenMachineException as e:
        print(f'Exception: {e.message}')

if __name__ == '__main__':
    main()