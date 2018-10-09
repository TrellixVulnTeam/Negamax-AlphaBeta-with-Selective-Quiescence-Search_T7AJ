from anytree import Node, RenderTree, PreOrderIter
import random


class TreeGenerator:
    def __init__(self, depth):
        self.root = Node(None)
        self.depth = depth

    def generate(self, b=0, h=0, v=0, approx=0, i=0, filename=None):
        """
        :param b: branching factor
        :param h: horizon
        :param v: desired value
        :param approx: approximation
        :param i: interestingness
        :param filename: if a .txt file with the correct format is given, then a tree will be produced exact to the file
        :return: A game tree
        """
        if filename is not None:
            file = open(filename, "r")
            for line in file:
                if line.startswith("Parent:"):
                    pass
                elif line.startswith("Child:"):
                    pass
                else:
                    print("File wrong format!")
                    break

        else:
            self.expand(self.root, b)
            nodelist = [node for node in PreOrderIter(self.root)]

            while self.root.height < self.depth:               # Only go up to depth Specified in the generator function
                for node in nodelist:
                    if node.is_leaf:                                                # expand leaf nodes
                        self.expand(node, b)
                        nodelist = [node for node in PreOrderIter(self.root)]       # update nodelist

            nodelist = [node for node in PreOrderIter(self.root)]                   # update nodelist
            for node in nodelist:
                if node.is_leaf:
                    node.name = self.random_value()                                 # assign values to all leaf nodes

    def display(self):
        for pre, fill, node in RenderTree(self.root):
            print("%s%s" % (pre, node.name))

    def random_value(self):
        return random.randint(1, 100+1)

    def expand(self, node, factor):     # expand node by factor of variable "factor"
        for i in range(0, factor):
            Node(self.random_value(), parent=node)

    def export(self, filename):
        """
        A function that exports the current state of the tree to a .txt file.
        The format will allow it to be filled back into the generate tree function
        :return: A .txt file
        """
        file = open(filename, "w+")

        nodelist = [node for node in PreOrderIter(self.root)]
        for node in nodelist:
            if node.is_leaf:
                continue
            childlist = node.children
            file.write("Parent: " + str(node.name) + "\n")
            for child in childlist:
                file.write("\tChild: " + str(child.name) + "\n")
