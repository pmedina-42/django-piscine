def main():
    values = {
        "int42": 42,
        "str42": "42",
        "qd": "quarante-deux",
        "fl42": 42.0,
        "t": True,
        "lst42": [42],
        "dct42": {42: 42},
        "tup42": (42,),
        "set42": set()
    }

    for name, value in values.items():
        print(f'{value} has a type {type(value)}')

if __name__ == "__main__":
    main()