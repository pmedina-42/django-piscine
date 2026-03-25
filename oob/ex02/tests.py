from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

def main():
    # Display hot beverage
    print(f'{HotBeverage().__str__()}\n')
    # Display coffee
    print(f'{Coffee().__str__()}\n')
    # Display tea
    print(f'{Tea().__str__()}\n')
    # Display chocolate
    print(f'{Chocolate().__str__()}\n')
    # Display cappuccino
    print(f'{Cappuccino().__str__()}')

if __name__ == '__main__':
    main()