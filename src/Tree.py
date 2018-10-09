from anytree import Node, RenderTree


class TreeGenerator:
    def __init__(self, root_item):
        self.root = Node(root_item)

    def generate(self, b, h, v, approx, i):
        """
        :param root: root node in the tree
        :param b: branching factor
        :param h: horizon
        :param v: desired value
        :param approx: approximation
        :param i: interestingness
        :return: A game tree
        """
        self.root = Node("udo")
        marc = Node("marc", parent=self.root)
        lian = Node("lian", parent=marc)
        dan = Node("dan", parent=self.root)
        jet = Node("jet", parent=dan)
        jan = Node("jan", parent=dan)
        joe = Node("joe", parent=dan)

    def display(self):
        for pre, fill, node in RenderTree(self.root):
            print("%s%s" % (pre, node.name))
