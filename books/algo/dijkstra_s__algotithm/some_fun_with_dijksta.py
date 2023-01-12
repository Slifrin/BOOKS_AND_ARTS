"""
    chapter 7
    This is about graphs with WEIGHTS
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

    def __init__(self, start: Node, end: Node, weight: int):
        self.start = start
        self.end = end
        self.weight = weight


def simple_graph_generation():
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    graph["a"] = {}
    graph["a"]["fin"] = 1

    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5

    graph["fin"] = {}

    pprint(graph)
    return graph


def simple_cost_table():
    infinity = float("inf")
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = infinity
    pprint(costs)
    return costs


def simple_parents_table():
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None
    pprint(parents)
    return parents


def find_lowest_cost_node(costs: dict[str, int], processed) -> str | None:
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra_algorithm():
    graph = simple_graph_generation()
    costs = simple_cost_table()
    parents = simple_parents_table()
    processed = []

    node: str | None = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    pprint(costs)
    print(f"Shortest path {costs['fin']}")

def main() -> None:
    print(f'Hello main from : {__file__}')
    dijkstra_algorithm()

if __name__ == '__main__':
    main()