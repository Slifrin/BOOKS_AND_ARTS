"""
    chapter 6
"""
from __future__ import annotations

from typing import Literal, Optional
from pprint import pprint
from collections import deque


class Node:
    def __init__(self, name: str, parent: Optional[Node]):
        self.name = name
        neighbours: set[Node] = set()
        if parent:
            neighbours.add(parent)


class Edge:
    def __init__(self, node1:Node, node2:Node):
        self.node1 = node1
        self.node2 = node2


def simeple_graph():
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
    pprint(graph)
    return graph


NUMBER_CHECKS: int = 0

def is_mango_seller(name: str) -> bool:
    global NUMBER_CHECKS
    NUMBER_CHECKS += 1
    return name == "peggy"


def breadth_first_search(name, acceptance_function):
    graph = simeple_graph()
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if acceptance_function(person):
                print(f"OH RIGHT {person} is mango seller!!!")
                return True
            else:
                search_queue += graph[person]
                searched.append(graph[person])
    return False


def main() -> None:
    print(f'Hello main from : {__file__}')
    breadth_first_search("bob", is_mango_seller)
    print(f"{NUMBER_CHECKS=}")

if __name__ == '__main__':
    main()