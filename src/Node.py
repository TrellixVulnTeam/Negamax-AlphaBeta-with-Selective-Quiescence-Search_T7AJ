class Node:

    def __init__(self, data, parent, depth=0):
        self.daughters = []     # For Daughters
        self.data = data
        self.parent = parent
        self.depth = depth
        self.height = 0         # TODO: figure this out

    def is_internal(self):
        if len(self.daughters) > 0:
            return True
        else:
            return False

    def is_daughter(self):
        if self.depth > 0:
            return True
        else:
            return False

    def is_root(self):
        if self.depth is 0:
            return True
        else:
            return False

    def is_leaf(self):
        if len(self.daughters) is 0:
            return True
        else:
            return False

    def add_daughter(self, data):
        self.daughters.append(Node(data, self))
