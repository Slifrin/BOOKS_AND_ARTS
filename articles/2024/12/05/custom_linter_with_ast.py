"""
requires instalation of flake8
https://www.youtube.com/watch?v=OjPT15y2EpE
"""

import ast

class NodeVisitor(ast.NodeVisitor):
    def visit_For(self, node: ast.AST):
        print(node)
        self.generic_visit(node)


def main() -> None:
    print(f'Hello main from : {__file__}')

    with open('file_to_check.py', 'r') as code_f:
        code = code_f.read()

    node = ast.parse(code)
    print(node)
    print(node._fields)

    NodeVisitor().visit(node)


if __name__ == '__main__':
    main()