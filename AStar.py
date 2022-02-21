from heapq import heapify, heappush, heappop
from Heuristics import euclidean_distance


def a_star(start, goal, heuristic, th=None):
    """
    Finds the shortest distance between two nodes using the A-star (A*) algorithm
    :param graph: an adjacency-matrix-representation of the graph where (x,y) is the weight of the edge or 0 if there is no edge.
    :param heuristic: an estimation of distance from node x to y that is guaranteed to be lower than the actual distance. E.g. straight-line distance
    :param start: the node to start from.
    :param goal: the node we're searching for
    :return: The shortest distance to the goal node. Can be easily modified to return the path.
    """

    # This contains the distances from the start node to all other nodes, initialized with a distance of "Infinity"
    # distances = [float("inf")] * len(graph)

    # The distance from the start node to itself is of course 0
    start.set_d(0)

    # This contains the priorities with which to visit the nodes, calculated using the heuristic.
    priorities = []
    heapify(priorities)

    # start node has a priority equal to straight line distance to goal. It will be the first to be expanded.
    start.set_h(heuristic(start, goal))
    heappush(priorities, (start.get_f(), start))

    # # This contains whether a node was already visited
    # visited = [False] * len(graph)

    # While there are nodes left to visit...
    while len(priorities) > 0:
        # ... find the node with the currently lowest priority...
        node = heappop(priorities)[-1]
        node.visit()
        if node == goal:
            return node

        if th and node.get_f() > th:
            return node.get_f()

        # print("Visiting node " + lowestPriorityIndex + " with currently lowest priority of " + lowestPriority)

        # ...then, for all neighboring nodes that haven't been visited yet....
        for neighbor_node in node.get_neighbors():

            # if neighbor_node.d < float('inf'):
            #     continue

                # ...if the path over this edge is shorter...
            if node.d + euclidean_distance(node, neighbor_node) < neighbor_node.d:
                    # ...save this path as new shortest path
                neighbor_node.set_prev(node)
                neighbor_node.set_d(node.d + euclidean_distance(node, neighbor_node))
                neighbor_node.set_h(heuristic(neighbor_node, goal))
                    # ...and set the priority with which we should continue with this node
                heappush(priorities, (neighbor_node.get_f(), neighbor_node))
                neighbor_node.see()
                    # print("Updating distance of node " + i + " to " + distances[i] + " and priority to " + priorities[i])

                # Lastly, note that we are finished with this node.
        # node.visit()
                # print("Visited nodes: " + visited)
                # print("Currently lowest distances: " + distances)
    # There was no node not yet visited --> Node not found
    return -1