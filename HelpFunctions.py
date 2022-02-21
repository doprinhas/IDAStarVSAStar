import time
import numpy as np




def get_time_passed(start_time, u="sec", r=2):
    time_sec = (time.time_ns() - start_time) / 10**9
    if u == "sec":
        return round(time_sec, r)
    elif u == "min":
        return round(time_sec / 60, r)
    elif u == "h":
        return round(time_sec / 3600, r)


def count_visited_more_than_once(nodes):
    count = 0
    for node_id, node in nodes.items():
        if node.times_visited() > 1:
            count += 1
    return count


def count_visited(nodes):
    count = 0
    for node_id, node in nodes.items():
        count += node.times_visited()
    return count


def count_saw(nodes):
    count = 0
    for node_id, node in nodes.items():
        count += node.times_saw()
    return count


def get_path(goal):
    path = []
    cur_node = goal
    while cur_node != None:
        path.append(cur_node.get_position())
        cur_node = cur_node.prev_node
    return path[::-1]

