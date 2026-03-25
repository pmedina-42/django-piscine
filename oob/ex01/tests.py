from intern import Intern

def main():
    # Two interns
    mark = Intern('Mark')
    noname = Intern()
    #Display names
    print(mark.__str__())
    print(noname.__str__())
    # Ask Mark to make a coffee and display the result
    coffee = mark.make_coffee()
    print(coffee.__str__())
    # Ask the other intern to work
    try:
        noname.work()
    except Exception as e:
        print(f'Exception: {e}')

if __name__ == '__main__':
    main()