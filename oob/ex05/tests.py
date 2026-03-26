from elements import Html, Head, Body, P, H1, Ul, Li, Img, Br
from elem import Text

def main():
    print(Html([Head(), Body()]))
    print(P(Text('Hello world')))
    print(H1('Title'))
    print(Ul(Li('A'), Li('B'), Li('C')))
    print(Img({"src": "image,png"}))
    print(Br())

if __name__ == '__main__':
    main()