from anytree import Node, RenderTree

def generate(b, h, v, approx, i):
    """
    :param b: branching factor
    :param h: horizon
    :param v: desired value
    :param approx: approximation
    :param i: interestingness
    :return: A game tree
    """
    udo = Node(1)
    marc = Node(2, parent=udo)
    lian = Node(3, parent=marc)
    dan = Node(4, parent=udo)
    jet = Node(5, parent=dan)
    jan = Node(6, parent=dan)
    joe = Node(7, parent=dan)

    for pre, fill, node in RenderTree(udo):
        print("%s%s" % (pre, node.name))