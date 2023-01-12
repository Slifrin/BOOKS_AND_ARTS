"""
    chapter 9 - knapsack problem
"""

from collections import namedtuple
from pprint import pprint


# def solve_knapsack_problem(items: dict[str, tuple[int, int]], knapsack_size: int) -> list[str]:
#     picked_items: list[str] = []

#     table: list[list[tuple[str, int, int]]] = []


#     # each cell ui
    
    
#     for product,(weight, value) in items.items():
#         i:int = 0
#         table.append([])
#         for j in range(knapsack_size + 1):
#             if i == 0:
#                 if j + 1 >= weight:
#                     table[i].append((product, weight, value))
#                 else:
#                     table[i].append(("DUMMY", 0, -1))
#             else:
#                 prevois_max = table[i - 1][j]

#                 reamaing_space_cell_max = 0
#                 if (j + 1 - weight) >= 0:
#                     reamaing_space_cell_max = table[i-1][j + 1 - weight][2]
#                 potential_new_max = reamaing_space_cell_max + value

#     return picked_items

def show_table(table):
    print()
    for row in table:
        print(row)
    print()

def common_substrings(world_a:str, world_b:str):
    """
        Diagonal is not only importatn place. 
    """
    cell = [[0] * len(world_b) for _ in range(len(world_a))]
    # show_table(cell)
    for r in range(len(world_a)):
        for c in range(len(world_b)):
            if world_a[r] == world_b[c]:
                old_valu = 0
                if r > 0 and c > 0:
                    old_valu = cell[r - 1][c -  1]
                cell[r][c] = old_valu + 1
            else:
                cell[r][c] = 0
    print(f"{world_a=}    {world_b=}")
    show_table(cell)


def check_substring():
    common_substrings("fish", "fishh")
    common_substrings("fish", "hish")
    common_substrings("blaaaabla", "blablaaaabla")


def longest_common_subsecuence(world_a:str, world_b:str):
    """
    """
    cell = [[0] * len(world_b) for _ in range(len(world_a))]

    for r in range(len(world_a)):
        for c in range(len(world_b)):
            if world_a[r] == world_b[c]:
                old_valu = 0
                if r > 0 and c > 0:
                    old_valu = cell[r - 1][c -  1]
                cell[r][c] = old_valu + 1
            else:
                old_a = 0
                if r > 0:
                    old_a = cell[r-1][c]
                old_b = 0
                if c > 0:
                    old_b = cell[r][c-1]
                cell[r][c] = max(old_a, old_b)
    print(f"{world_a=}    {world_b=}")
    show_table(cell)


def subsecuence():
    longest_common_subsecuence("fort", "fosh")
    longest_common_subsecuence("fish", "fosh")



def main() -> None:
    print(f'Hello main from : {__file__}')
    subsecuence()

if __name__ == '__main__':
    main()