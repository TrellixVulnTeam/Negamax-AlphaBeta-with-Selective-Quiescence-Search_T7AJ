class Node:

    def __init__(self, data, parent):
        self.daughters = []     # For Daughters
        self.data = data
        self.parent = parent
        self.depth = 0
        self.height = 0         # TODO: figure this out

    def is_parent(self):
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
