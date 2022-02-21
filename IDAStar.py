import numpy as np
from Heuristics import euclidean_distance
import HelpFunctions as Functions
import AStar

def iterative_deepening_a_star(nodes, start, goal, heuristic):
    """
    Performs the iterative deepening A Star (A*) algorithm to find the shortest path from a start to a target node.
    Can be modified to handle graphs by keeping track of already visited nodes.
    :param tree:      An adjacency-matrix-representation of the tree where (x,y) is the weight of the edge or 0 if there is no edge.
    :param heuristic: An estimation of distance from node x to y that is guaranteed to be lower than the actual distance. E.g. straight-line distance.
    :param start:      The node to start from.
    :param goal:      The node we're searching for.
    :return: number shortest distance to the goal node. Can be easily modified to return the path.
    """
    iter_count = 0
    threshold = heuristic(start, goal)
    start.set_d(0); start.set_h(threshold)
    while True:
        # print("Iteration with threshold: " + str(threshold))
        iter_count += 1
        # print(f"Iteration: {iter_count} with threshold: {str(threshold)} nodes: {Functions.count_visited(nodes)}" )
        # distance = iterative_deepening_a_star_rec(start, goal, heuristic, threshold)
        distance = AStar.a_star(start, goal, heuristic, threshold)
        if distance == float("inf"):
            # Node not found and no more nodes to visit
            return -1
        elif distance == goal:
            # if we found the node, the function returns the negative distance
            print(f"Iteration: {iter_count}")
            return goal
        else:
            # if it hasn't found the node, it returns the (positive) next-bigger threshold
            threshold = distance
            for id, node in nodes.items():
                node.d = float('inf')
            start.set_d(0)

def iterative_deepening_a_star_rec(node, goal, heuristic, threshold):
    """
    Performs DFS up to a depth where a threshold is reached (as opposed to interative-deepening DFS which stops at a fixed depth).
    Can be modified to handle graphs by keeping track of already visited nodes.
    :param tree:      An adjacency-matrix-representation of the tree where (x,y) is the weight of the edge or 0 if there is no edge.
    :param heuristic: An estimation of distance from node x to y that is guaranteed to be lower than the actual distance. E.g. straight-line distance.
    :param node:      The node to continue from.
    :param goal:      The node we're searching for.
    :param distance:  Distance from start node to current node.
    :param threshold: Until which distance to search in this iteration.
    :return: number shortest distance to the goal node. Can be easily modified to return the path.
     """
    # print("Visiting Node " + str(node))
    node.see()
    if node == goal:
        # We have found the goal node we we're searching for
        return node

    estimate = node.get_f()
    # print(node.id, estimate)
    if estimate > threshold:
        # print("Breached threshold with heuristic: " + str(estimate))
        return estimate

    # ...then, for all neighboring nodes....
    node.visit()
    min = float("inf")
    for neighbor_node in node.get_neighbors():
        # neighbor_node.see()
        dis = node.d + euclidean_distance(neighbor_node, node)
        if neighbor_node.d <= dis:
            continue
        neighbor_node.set_d(dis)
        neighbor_node.set_h(heuristic(neighbor_node, goal))
        t = iterative_deepening_a_star_rec(neighbor_node, goal, heuristic, threshold)
        if t == goal:
            # Node found
            neighbor_node.set_prev(node)
            return t
        elif t < min:
            min = t

    return min
