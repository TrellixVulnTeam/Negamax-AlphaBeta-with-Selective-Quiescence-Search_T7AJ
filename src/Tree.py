from Node import Node
import random


class Tree:

    root = Node(None, None)

    def __init__(self, b, h, v, approx, i):
        """
        :param b:   Branching Factor
        :param h:   Horizon
        :param v:   Expected Value
        :param approx:  Approximation (Smudge values with this)
        :param i:   interesting value
        """
        self.branching_factor = b
        self.horizon = h
        self.root = Node(v, None)   # Value we expect to get is the root
        self.approx = approx
        self.interestingness = i

    def root(self):
        return self.root

    def generate(self):
        nodes_toexpand = []
        nodes_toexpand.append(self.root)
        for i in range(0, self.horizon):
            for node in nodes_toexpand:
                nodes_toexpand = self.expand(node, self.branching_factor)[:]


    @staticmethod
    def expand(node, branching_factor):
        for i in range(0, branching_factor):
            node.daughters.append(Node(random.randint(1, 100), node))
            node.daughters[-1].depth = node.daughters[-1].parent.depth + 1
        return node.daughters

    def display(self):
        print(self.root.data)
        for node in self.root.daughters:
            print(node.data)
