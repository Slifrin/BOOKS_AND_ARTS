import pygame
from random import random
from collections import deque

cols = 25  # 25
rows = 15  # 15
TILE = 30


def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2


def get_next_nodes(x, y):
    check_next_node = (
        lambda x, y: True
        if 0 <= x < cols and 0 <= y < rows and not grid[y][x]
        else False
    )
    ways = [-1, 0], [0, -1], [1, 0], [0, 1] #, [-1, 1], [1, 1], [-1, -1], [1, -1]
    return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]


def get_click_mouse_pos():
    x, y = pygame.mouse.get_pos()
    grid_x, grid_y = x // TILE, y // TILE
    pygame.draw.rect(screen, pygame.Color('red'), get_rect(grid_x, grid_y))
    click = pygame.mouse.get_pressed()

    return (grid_x, grid_y) if click[0] else False


def bfs(start, goal, graph):
    queue = deque([start])
    visited = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node

    return queue, visited

pygame.init()
screen = pygame.display.set_mode((cols * TILE, rows * TILE))
clock = pygame.time.Clock()
running = True


grid = [[1 if random() < 0.2 else 0 for col in range(cols)] for row in range(rows)]
graph = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if not col:
            graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)

start = (0, 0)
goal = start
queue = deque([start])
visited = {start: None}


print(queue)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    [
        [
            pygame.draw.rect(
                screen,
                pygame.Color("darkorange"),
                get_rect(x, y),
                border_radius=TILE // 5,
            )
            for x, col in enumerate(row)
            if col
        ]
        for y, row in enumerate(grid)
    ]

    [
        pygame.draw.rect(screen, pygame.Color("forestgreen"), get_rect(x, y))
        for x, y in visited
    ]
    [
        pygame.draw.rect(screen, pygame.Color("darkslategray"), get_rect(x, y))
        for x, y in queue
    ]

    # bfs
    mouse_pos = get_click_mouse_pos()
    if mouse_pos and not grid[mouse_pos[1]][mouse_pos[0]]:
        queue, visited = bfs(start, mouse_pos, graph)
        goal = mouse_pos

    # draw path
    path_head, path_segment = goal, goal

    while path_segment:
        pygame.draw.rect(screen, pygame.Color("white"), get_rect(*path_segment), TILE, border_radius=TILE // 3)
        path_segment = visited[path_segment]

    pygame.draw.rect(screen, pygame.Color("blue"), get_rect(*start), TILE, border_radius=TILE // 3)
    pygame.draw.rect(screen, pygame.Color("magenta"), get_rect(*path_head), TILE, border_radius=TILE // 3)

    pygame.display.flip()

    clock.tick(7)

pygame.quit()
