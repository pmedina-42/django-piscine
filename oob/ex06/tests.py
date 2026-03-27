from Page import Page
from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br
from elem import Elem

def test_html():
    print('HTML tests:')

    # Invalid page with no head
    page = Page(
        Html([
            Body([])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: False')
    #print(page)

    # Invalid page with no body
    page = Page(
        Html([
            Head([])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: False')
    #print(page)

    # Valid page with empty body
    page = Page(
        Html([
            Head([Title('XD')]),
            Body([])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: True')
    #print(page)

def test_head():
    print('Head tests:')

    # Invalid page with empty head
    page = Page(
        Html([
            Head([]),
            Body([])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: False')
    #print(page)

    # Valid page with one title
    page = Page(
        Html([
            Head([Title('XD')]),
            Body([])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: True')
    #print(page)

    # Invalid page with two titles
    page = Page(
        Html([
            Head([Title('XD'), Title('XDD')]),
            Body([])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: False')
    #print(page)

    print(' - Meta:')
    test_meta()

def test_body_content():
    print('Body content tests:')

    print(' - Ul:')
    test_list(Ul)

    print(' - Ol:')
    test_list(Ol)

    print(' - H1:')
    test_header(H1)

    print(' - H2:')
    test_header(H2)

    print(' - Table:')
    test_table()

    print(' - Div / Span:')
    test_div_span()

    print(' - P:')
    test_p()


def test_list(list_type):
    # Valid page with well formatted Ol
    page = Page(
        Html([
            Head([Title('Whatever')]),
            Body([list_type([
                Li('A'),
                Li('B'),
                Li('C')
            ])])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: True')
    #print(page)

    # Invalid page with P inside Li
    page = Page(
        Html([
            Head([Title('Whatever')]),
            Body([list_type([
                Li('A'),
                Li(P('Bad')),
                Li('C')
            ])])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: False')
    #print(page)

    # Invalid page with != Li
    page = Page(
        Html([
            Head([Title('Whatever')]),
            Body([list_type([
                Li('A'),
                Li('B'),
                P('Bad')
            ])])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: False')
    #print(page)

    # Invalid page without Li
    page = Page(
        Html([
            Head([Title('Whatever')]),
            Body([list_type([])])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: False')
    #print(page)

def test_header(header_type):
    # Valid header
    page = Page(
        Html([
            Head([Title('Whatever')]),
            Body([header_type('Valid header')])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: True')
    #print(page)

    # Invalid header
    page = Page(
        Html([
            Head([Title('Whatever')]),
            Body([header_type([P('A')])])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: False')
    #print(page)

def test_table():
    # Valid table
    page = Page(
        Html([
            Head([Title('Test 4: table')]),
            Body([Table([
                Tr([Th('Name'), Th('Last name')]),
                Tr([Td('Patricia'), Td('Medina')])
            ])])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: True')
    #print(page)

    # Invalid table with Th and Tr inside Td
    page = Page(
        Html([
            Head([Title('Test 4: table')]),
            Body([Table([
                Tr([Th('Name'), Td('Last name')])
            ])])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: False')
    #print(page)

    # Valid table without Th and multiple Tr
    page = Page(
        Html([
            Head([Title('Test 4: table')]),
            Body([Table([
                Tr([Td('xD'), Td('xDD')]),
                Tr([Td('xD'), Td('xDD')])
            ])])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: True')
    #print(page)

    # Valid table without Tr and multiple Th
    page = Page(
        Html([
            Head([Title('Test 4: table')]),
            Body([Table([
                Tr([Th('xD'), Th('xDD')]),
                Tr([Th('xD'), Th('xDD')])
            ])])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: True')
    #print(page)

    # Invalid empty table
    page = Page(
        Html([
            Head([Title('Test 4: table')]),
            Body([Table([])])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: False')
    #print(page)

def test_meta():
    # Valid meta
    page = Page(
        Html([
            Head([
                Title('Test'),
                Meta(attr={'charset': 'UTF-8'})
            ]),
            Body([])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: True')

    # Invalid meta with content
    try:
        page = Page(
            Html([
                Head([
                    Title('Test'),
                    Meta(content='Bad')
                ]),
                Body([])
            ])
        )
    except Elem.ValidationError:
        print(f'Valid: False. Expected: False')

def test_p():
    # Valid paragraph
    page = Page(
        Html([
            Head([Title('Test')]),
            Body([
                P('Hello world')
            ])
        ])
    )
    print(f'Valid: {page.is_valid()}. Expected: True')

    # Invalid paragraph with block element inside
    try:
        page = Page(
            Html([
                Head([Title('Test')]),
                Body([
                    P(Div('Bad'))
                ])
            ])
        )
    except Elem.ValidationError:
        print(f'Valid: False. Expected: False')


def test_div_span():
    # Valid nesting
    try:
        
        page = Page(
            Html([
                Head([Title('Test')]),
                Body([
                    Div([P('XD')])
                ])
            ])
        )
    except Elem.ValidationError:
        print(f'Valid: False. Expected: True')

    # Invalid span with block element
    try:
        page = Page(
            Html([
                Head([Title('Test')]),
                Body([
                    Span(Div('Bad'))
                ])
            ])
        )
    except Elem.ValidationError:
        print(f'Valid: False. Expected: False')

    page = Page(
    Html([
        Head([Title('Test')]),
        Body([
            Div([
                Span('Paragraph inside div')
            ])
        ])
    ])
)
    print(f'Valid: {page.is_valid()}. Expected: True')


if __name__ == '__main__':
    test_html()
    test_head()
    test_body_content()
    