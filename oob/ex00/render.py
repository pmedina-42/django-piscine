import sys


def load_settings():
    settings = {}
    try:
        with open('settings.py', 'r') as f:
            code = f.read()
        exec(code, settings)
    except FileNotFoundError:
        print('Error: settings.py not found.')
        sys.exit(1)
    return settings

def render_template(template_path: str, settings: dict):
    try:
        with open(template_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print('Error: template file not found.')
        sys.exit(1)
    for key, value in settings.items():
        if not key.startswith('__'):
            content = content.replace(f'{{{key}}}', str(value))
    return content

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 render.py <file.template>')
        sys.exit(1)
    template_path = sys.argv[1]
    if not template_path.endswith('.template'):
        print('Error: file must have a .template extension.')
        sys.exit(1)

    settings = load_settings()
    output = render_template(template_path, settings)
    output_path = template_path.replace('.template', '.html')
    with open(output_path, 'w') as f:
        f.write(output)

if __name__ == "__main__":
    main()