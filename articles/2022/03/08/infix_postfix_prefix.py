
from enum import Enum

class NodeType(Enum):
    EMPTY = 0
    NUMBER = 1
    ADD = 2
    SUB = 3
    MUL = 4
    DIV = 5


class Node:
    def __init__(self):
        self.parent = None
        self.l_child = None
        self.r_child = None
        self.value = None
        self.node_type = NodeType.EMPTY

def get_root_node(last_used_node:Node):
    checked_node = last_used_node
    while last_used_node.parent is not None:
        checked_node = checked_node.parent
    return checked_node

def add_node(current_node, new_node:Node):
    if new_node.node_type == NodeType.NUMBER:
        if current_node is None:
            return new_node
        

def parse_equation(equation:str):
    nodes = []
    current_node = None
    for c in equation:
        new_node = Node()
        if c.isdigit():
            new_node.node_type = NodeType.NUMBER
            new_node.value = float(c)
        elif c == "+":
            new_node.node_type = NodeType.ADD
        elif c == "-":
            new_node.node_type = NodeType.SUB
        elif c == "*":
            new_node.node_type = NodeType.MUL
        elif c == "/":
            new_node.node_type = NodeType.DIV
        
        current_node = add_node(nodes, new_node)

    return get_root_node(current_node), nodes





def main():
    print(f'Hello main from : {__file__}')
    # equation = "1+2+3*4-5/6+(7*8(9+1))"
    equation = "1+2+3"

if __name__ == '__main__':
    main()