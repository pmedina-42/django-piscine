from elem import Elem, Text
from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br

class Page:
    def __init__(self, root: Elem):
        if not isinstance(root, Elem):
            raise TypeError('Page root must be an Elem instance')
        self.root = root

    def is_valid(self):
        return self._validate_node(self.root)

    def __str__(self):
        html = str(self.root)
        if isinstance(self.root, Html):
            return '<!DOCTYPE html>\n' + html
        return html

    def write_to_file(self, filename):
        with open(filename, 'w', encoding = 'utf-8') as f:
            f.write(str(self))

    allowed_tags = {
        Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td,
        Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br
    }

    def _validate_node(self, node):
        if not isinstance(node, tuple(self.allowed_tags)):
            return False
        if isinstance(node, Html):
            if len(node.content) != 2:
                return False
            if not isinstance(node.content[0], Head):
                return False
            if not isinstance(node.content[1], Body):
                return False
        if isinstance(node, Head):
            titles = [c for c in node.content if isinstance(c, Title)]
            if len(titles) != 1:
                return False
        if isinstance(node, Body) or isinstance(node, Div):
            for c in node.content:
                if not isinstance(c, (H1, H2, Div, Table, Ul, Ol, Span, Text, P)):
                    return False
        if isinstance(node, (Title, H1, H2, Li, Th, Td)):
            if len(node.content) != 1:
                return False
            if not isinstance(node.content[0], Text):
                return False
        if isinstance(node, P):
            if len(node.content) != 1 or not isinstance(node.content[0], Text):
                return False
        if isinstance(node, Span):
            for c in node.content:
                if not isinstance(c, Text):
                    return False
        if isinstance(node, (Ul, Ol)):
            if len(node.content) == 0:
                return False
            if not all(isinstance(c, Li) for c in node.content):
                return False
        if isinstance(node, Tr):
            if len(node.content) == 0:
                return False
            if not all(isinstance(c, (Th, Td)) for c in node.content):
                return False
            has_th = any((isinstance(c, Th)) for c in node.content)
            has_td = any((isinstance(c, Td)) for c in node.content)
            if has_td and has_th:
                return False
        if isinstance(node, Table):
            if len(node.content) == 0:
                return False
            if not all(isinstance(c, Tr) for c in node.content):
                return False
        
        for child in node.content:
            if isinstance(child, Elem):
                if not self._validate_node(child):
                    return False

        return True
