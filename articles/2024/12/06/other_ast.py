import ast
from pprint import pprint


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {'import': [], 'from': []}

    def visit_Import(self, node: ast.Import):
        for name in node.names:
            self.stats['import'].append(name.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        for name in node.names:
            self.stats['from'].append(name.name)
        self.generic_visit(node)

    def report(self):
        pprint(self.stats)



def main() -> None:
    print(f'Hello main from : {__file__}')
    with open('other_ast.py', 'r') as code_f:
        tree = ast.parse(code_f.read())

    analyzer = Analyzer()
    analyzer.visit(tree)
    analyzer.report()


if __name__ == '__main__':
    main()