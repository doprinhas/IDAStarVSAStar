import numpy as np
from Node import Node


def simple_graph(size=(100, 100), diagonal_pass=True):
    graph = np.zeros(size)
    nodes = {}
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            pos = (i, j)
            id = str(pos)
            nodes[id] = Node(id, pos)

    set_nodes_neighbors(nodes, graph, diagonal_pass)
    d = 2
    return graph, nodes, nodes[str((0+d, 0+d))], nodes[str((len(graph)-d, len(graph[0])-d))]


def blocks_graph(size=(100, 100), diagonal_pass=True):
    graph = np.zeros(size)
    for i in range(0, len(graph), 2):
        block = np.random.randint(0, len(graph[i]), int(len(graph[i])/4))
        graph[i][block] = 1
    d = 2
    graph[(0+d, 0+d)] = 0
    graph[(len(graph)-1, len(graph[0])-1)] = 0
    nodes = {}
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                pos = (i, j)
                id = str(pos)
                nodes[id] = Node(id, pos)
    set_nodes_neighbors(nodes, graph, diagonal_pass)
    return graph, nodes, nodes[str((0+d, 0+d))], nodes[str((len(graph)-1, len(graph[0])-1))]


def complex_graph(size=(100, 100), diagonal_pass=True):
    graph = np.zeros(size)
    for i in range(0, len(graph), 8):
        graph[i][:int(len(graph[i])*0.75)] = 1

    for i in range(4, len(graph), 8):
        graph[i][int(len(graph[i])*0.25):] = 1

    for i in range(0, len(graph), 2):
        block = np.random.randint(0, len(graph[i]), int(len(graph[i])/4))
        graph[i][block] = 1
    d = 2
    graph[(0+d, 0+d)] = 0
    graph[(len(graph)-1, len(graph[0])-1)] = 0
    nodes = {}
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                pos = (i, j)
                id = str(pos)
                nodes[id] = Node(id, pos)
    set_nodes_neighbors(nodes, graph, diagonal_pass)
    return graph, nodes, nodes[str((0+d, 0+d))], nodes[str((len(graph)-1, len(graph[0])-1))]

def set_nodes_neighbors(nodes, graph, diagonal_pass):
    for node_id, node in nodes.items():
        node.set_neighbors(get_neighbors(nodes, graph, node, diagonal_pass))


def get_neighbors(nodes, graph, node, diagonal_pass):
    neighbors = []
    x, y = node.get_position()
    if is_valid_cell(graph, x+1, y):
        neighbors.append(nodes[str((x+1, y))])
    if is_valid_cell(graph, x-1, y):
        neighbors.append(nodes[str((x-1, y))])
    if is_valid_cell(graph, x, y+1):
        neighbors.append(nodes[str((x, y+1))])
    if is_valid_cell(graph, x, y-1):
        neighbors.append(nodes[str((x, y-1))])
    if diagonal_pass:
        if is_valid_cell(graph, x+1, y+1):
            neighbors.append(nodes[str((x+1, y+1))])
        if is_valid_cell(graph, x-1, y+1):
            neighbors.append(nodes[str((x-1, y+1))])
        if is_valid_cell(graph, x+1, y-1):
            neighbors.append(nodes[str((x+1, y-1))])
        if is_valid_cell(graph, x-1, y-1):
            neighbors.append(nodes[str((x-1, y-1))])
    return neighbors


def is_valid_cell(graph, x, y):
    if x < 0 or y < 0:
        return False
    if x >= len(graph) or y >= len(graph[0]):
        return False
    if graph[x, y] == 1:
        return False
    return True