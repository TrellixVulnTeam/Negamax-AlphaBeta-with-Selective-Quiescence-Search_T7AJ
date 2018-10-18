"""
Name: Sabeer Bakir
Student No.: 16333886
Email: sabeer.bakir@ucdconnect.ie
"""
import random


class Node:

    def __init__(self, static_evaluation_val, parent, interesting_threshold=0):
        self.daughters = []     # For Daughters
        self.static_evaluation_val = static_evaluation_val
        self.parent = parent
        self.height = 0
        self.update_height(self)
        if parent is not None:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0
        self.interesting = random.randint(0, 100)       # random interesting value
        self.is_interesting = False

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

    def add_daughter(self, static_evaluation_val):
        self.daughters.append(Node(static_evaluation_val, self))

    def siblings(self):
        if self.is_root():
            return None
        else:
            return self.parent.daughters

    def update_height(self, node, update=1):
        if node.parent is None:
            return None
        else:
            node.parent.height = 0
            node.parent.height += update
            return self.update_height(node.parent, update + 1)
