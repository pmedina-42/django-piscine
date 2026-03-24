def main():
    try:
        with open('numbers.txt') as f:
            content = f.read().strip().split(',')
            for num in content:
                print(num)
    except Exception as e:
        print('Shit happens')

if __name__ == "__main__":
    main()