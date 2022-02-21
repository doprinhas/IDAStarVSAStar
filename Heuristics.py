import numpy as np


def euclidean_distance(node, goal):
    goal_pos = np.array(goal.get_position())
    node_pos = np.array(node.get_position())
    dis = (goal_pos - node_pos) ** 2
    dis = np.sum(dis)
    return round(np.sqrt(dis), 3)


def manhattan_distance(node, goal):
    goal_pos = np.array(goal.get_position())
    node_pos = np.array(node.get_position())
    dis = (goal_pos - node_pos)
    return round(np.sum(dis)/2, 3)


def diagonal_distance(node, goal):
    goal_pos = np.array(goal.get_position())
    node_pos = np.array(node.get_position())
    dis = (goal_pos - node_pos)
    return round(np.sum(dis) - np.min(dis), 3)