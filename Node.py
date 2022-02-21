

class Node:

    def __init__(self, id, pos, neighbors=[]):
        self.id = id
        self.pos = pos
        self.neighbors = neighbors
        self.prev_node = None
        self.visited = 0
        self.saw = 0
        self.h = float('inf')
        self.d = float('inf')

    def get_id(self):
        return self.id

    def get_position(self):
        return self.pos

    def get_neighbors(self):
        return self.neighbors

    def get_f(self):
        return self.d + self.h

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

    def set_h(self, h):
        self.h = h

    def set_d(self, d):
        self.d = d

    def set_prev(self, node):
        # if node in self.neighbors:
        #     self.neighbors.remove(node)
        self.prev_node = node

    def visit(self):
        self.visited += 1

    def see(self):
        self.saw += 1

    def times_visited(self):
        return self.visited

    def times_saw(self):
        return self.saw

    def reset(self):
        self.prev_node = None
        self.visited = 0
        self.saw = 0
        self.h = float('inf')
        self.d = float('inf')

    def __gt__(self, other):
        return True