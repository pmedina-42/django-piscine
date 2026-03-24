def load_table_elements(filename='periodic_table.txt'):
    elements = {}
    try:
        with open(filename) as f:
            for line in f:
                key, values = line.strip().split('=', 1)
                elements[key.strip()] = {k.strip(): v.strip() for k, v in (prop.split(':', 1) for prop in values.split(','))}
    except Exception as e:
        print('Shit happens')
    return elements

def generate_html(elements: dict):
    html_head_str = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Periodic table</title>
        </head>
        <body>
            <table>
    """
    html_end_str = """
                </td>
            </table>
        </body>
        </html>
    """
    html_table_str = '<tr>'
    current_pos = 0
    for name, value in elements.items():
        pos = int(value['position'])

        while current_pos < pos:
            html_table_str += """
                <td style="border: 1px solid white; padding:10px"></td>
            """
            current_pos += 1

        html_table_str += f"""
            <td style="border: 1px solid black; padding:10px">
                <h4>{name}</h4>
                <ul>
                    <li>No {value['number']}</li>
                    <li>{value['small']}</li>
                    <li>{value['molar']}</li>
                    <li>{value['electron']} electron</li>
                    <ul>
            </td>
        """

        current_pos += 1

        if current_pos == 18:
            html_table_str += "</tr><tr>"
            current_pos = 0

    with open('periodic_table.html', 'w') as f:
        f.write(html_head_str + html_table_str + html_end_str)

def main():
    generate_html(load_table_elements())

if __name__ == "__main__":
    main()