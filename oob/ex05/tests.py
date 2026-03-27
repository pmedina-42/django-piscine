from elements import Html, Head, Body, P, H1, Ul, Li, Img, Br
from elem import Text

def main():
    page = Html([
        Head([
            H1('"Hello ground!"')
        ]),
        Body([
            H1('"Oh no, not again!"'),
            Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
        ])
    ])
    html_output = str(page).replace('&quot;', '"')
    print(html_output)

if __name__ == '__main__':
    main()