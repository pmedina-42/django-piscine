import sys

def find_dict_key(d: dict, value: str):
    return next((k for k, v in d.items() if v == value), None)

def print_whatever(value: str):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    for k, v in states.items():
        if value.lower() == k.lower():
            print(f'{capital_cities[v]} is the capital of {k}')
            return
    for k, v in capital_cities.items():
        if value.lower() == v.lower():
            print(f'{v} is the capital of {find_dict_key(states, k)}')
            return
    print(f'{value} is neither a capital city nor a state')

def main():
    if (len(sys.argv) == 2):
        for value in sys.argv[1].split(','):
            if not value.isspace():
                print_whatever(value.strip())


if __name__ == "__main__":
    main()