import ast
import argparse

from typing import NamedTuple
from collections.abc import Iterator

from flake8.options.manager import OptionManager


class Flake8ASTErrorInfo(NamedTuple):
    line_number: int
    offset: int
    msg: str
    cls: type


class LocalImportsNotAllowed:
    msg = "J101 local imports are not allowed"

    @classmethod
    def check(cls, node: ast.FunctionDef, errors: list[Flake8ASTErrorInfo]) -> None:
        for child in node.body:
            if isinstance(child, (ast.Import, ast.ImportFrom)):
                err = Flake8ASTErrorInfo(child.lineno, child.col_offset, cls.msg, cls)
                errors.append(err)


class JurekASTVisitor(ast.NodeVisitor):

    msg = "J101 local imports are not allowed"

    def __init__(self):
        self.errors: list[Flake8ASTErrorInfo] = []

    def visit_FunctionDef(self, node: ast.FunctionDef):
        # better to loop over ast.walk(node)

        LocalImportsNotAllowed.check(node, self.errors)
        self.generic_visit(node)


class JurekASTPlugin:

    name = "flake8_jurek_ast_check"
    version = "0.0.0"

    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self):
        # print('running')
        # yield Flake8ASTErrorInfo(1, 0, "J1 complais a lot", type(self))
        visitor = JurekASTVisitor()
        visitor.visit(self._tree)
        yield from visitor.errors


    @staticmethod
    def add_options(option_manager: OptionManager):
        option_manager.add_option(
            '--some-custom-var',
            type=int,
            metavar='n', # shows in help text
            default=0,
            parse_from_config=True,
            help='Some custom var description. (Default: %(default)s)'
        )

    @staticmethod
    def parse_options(options: argparse.Namespace):
        if options.some_custom_var > 0:
            ...