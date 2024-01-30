import ast
import operator


def parser(text):
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
    }

    node = ast.parse(text, mode="eval")
    print(ast.dump(node, indent=4))
    node_body = node.body

    val = operators[type(node_body.op)](node_body.left.n, node_body.right.n)
    return val


def maybe_better_parse(text):
    """
    Helpfull link https://stackoverflow.com/questions/52819981/how-do-you-compile-an-ast-expr
    """
    print(f"running {maybe_better_parse.__name__}")
    print(ast.dump(ast.parse('123', mode='eval'), indent=4))
    node = ast.parse(text, "eval")
    print(type(node))
    print(node.body)
    print(node.body[0])

    print(ast.dump(node, indent=2))

    print(eval(text))
    print(exec(text))  # this do no not work
    # compiled_code = compile(node, filename="<string>", mode="eval") # same as this
    # val = eval(compiled_code)
    # print(val)
    print(eval(compile(ast.parse('123', mode="eval"), filename="<string>", mode="eval")))

    dump_code = ast.dump(node.body[0])
    compiled_code = compile(dump_code, filename="<string>", mode="eval")
    val = eval(compiled_code)
    print(val)

    print(ast.literal_eval(node))

    print(f"Finished {maybe_better_parse.__name__}")

def simple_example():
    # Creating AST
    code = ast.parse("print([1,2,3,4,5])")  
    # Printing AST
    print(ast.dump(code, indent=2))
    # Executing AST
    exec(compile(code, filename="", mode="exec"))

def experiment():
    print(f"Running {experiment.__name__}")
    code = '1+1'
    expr = ast.parse(code, mode="exec")
    # expr = ast.parse(code, mode="eval").body[0]
    print(type(expr))
    # compile(ast.Expression(expr), 'string', "eval")
    print(ast.dump(expr, indent=2))
    compiled_code = compile(expr, "<string>", mode="exec")
    print(compiled_code)
    print("Some output --> ", exec(compiled_code))

def experiment_2():
    print(f"Running {experiment_2.__name__}")
    tree = ast.parse("print('hello world')")
    # tree = ast.parse("1+1")
    print(tree)
    print(type(tree))
    print(ast.dump(tree, indent=2))
    exec(compile(tree, filename="<ast>", mode="exec"))

def experiment_3():
    print(f"Running {experiment_3.__name__}")
    tree = ast.parse("1+1", mode="eval")
    print(tree)
    print(type(tree))
    print(ast.dump(tree, indent=2))
    print(eval(compile(tree, filename="<ast>", mode="eval")))

def experiment_4(text):
    print(f"Running {experiment_4.__name__}")
    tree = ast.parse(text, mode="eval")
    print(tree)
    print(type(tree))
    print(ast.dump(tree, indent=2))
    print(eval(compile(tree, filename="<ast>", mode="eval")))

def experiment_5(text):
    print(f"Running {experiment_5.__name__}")

    tree = ast.parse(text, mode="eval")
    print(eval(compile(tree, filename="<ast>", mode="eval")))


def main() -> None:
    print(f"Hello main from : {__file__}")
    print(parser("7 + 13"))
    simple_example()
    # print(maybe_better_parse("7 + 13"))
    experiment()
    experiment_2()
    experiment_3()
    experiment_4("7 + 13")
    experiment_5("7 + 13")


if __name__ == "__main__":
    exit(main())
