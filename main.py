import numpy as np
import time
import matplotlib.pyplot as plt

import Graphs
import Heuristics
import AStar
import IDAStar
import HelpFunctions as Functions
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/2

def print_board(graph, start, goal):
    a = np.zeros(graph.shape)
    for i in range(graph.shape[0]):
        for j in range(graph.shape[1]):
            if graph[i][j] == 0:
                a[i][j] = 6
            if graph[i][j] == 1:
                a[i][j] = 2
            if str((i, j)) in nodes and nodes[str((i, j))].times_visited():
                a[i][j] = 3
                if nodes[str((i, j))].times_visited() > 1:
                    a[i][j] = 4
    for pos in Functions.get_path(goal):
        a[pos] = 1

    a[start.get_position()] = 8
    a[goal.get_position()] = 0
    plt.imshow(a, cmap=plt.cm.Set1)
    plt.show()

heuristics = [Heuristics.euclidean_distance, Heuristics.manhattan_distance, Heuristics.diagonal_distance]
# graphs = [Graphs.simple_graph, Graphs.manhattan_distance, Graphs.complex_graph]
# for heuristic in heuristics:
heuristics = Heuristics.diagonal_distance
graph, nodes, start, goal = Graphs.blocks_graph((20, 20), False)
# print_board(graph, start, goal)
#
st = time.time_ns()
AStar.a_star(start, goal, Heuristics.euclidean_distance)
print(Functions.get_time_passed(st, r=5))
print(Functions.count_visited(nodes), Functions.count_saw(nodes), Functions.count_visited_more_than_once(nodes))
print(Functions.get_path(goal))
print(goal.d)
print_board(graph, start, goal)

for node_n, node in nodes.items():
    node.reset()

st = time.time_ns()
IDAStar.iterative_deepening_a_star(nodes, start, goal, Heuristics.euclidean_distance)
print(Functions.get_time_passed(st, r=5))
print(Functions.count_visited(nodes), Functions.count_saw(nodes), Functions.count_visited_more_than_once(nodes))
print(Functions.get_path(goal))
print_board(graph, start, goal)

#
