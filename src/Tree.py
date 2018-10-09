from anytree import Node, RenderTree, PreOrderIter
import random


class TreeGenerator:
    def __init__(self, depth):
        self.root = Node(self.random_value())
        self.depth = depth

    def generate(self, b, h, v, approx, i):
        """
        :param b: branching factor
        :param h: horizon
        :param v: desired value
        :param approx: approximation
        :param i: interestingness
        :return: A game tree
        """
        self.expand(self.root, b)
        nodelist = [node for node in PreOrderIter(self.root)]

        while self.root.height < self.depth:
            for node in nodelist:
                if node.is_leaf:
                    self.expand(node, b)
                    nodelist = [node for node in PreOrderIter(self.root)]

    def display(self):
        for pre, fill, node in RenderTree(self.root):
            print("%s%s" % (pre, node.name))

    def random_value(self):
        return random.randint(1, 100+1)

    def expand(self, node, factor):     # expand node by factor of variable "factor"
        for i in range(0, factor):
            Node(self.random_value(), parent=node)
