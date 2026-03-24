import sys

def find_dict_key(d: dict, value: str):
    return next((k for k, v in d.items() if v == value), None)

def main():
    if (len(sys.argv) == 2):
        capital = sys.argv[1]
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
        if capital in capital_cities.values():
            state = find_dict_key(states, find_dict_key(capital_cities, capital))
            print(state)
        else:
            print('Unknown capital city')

if __name__ == "__main__":
    main()