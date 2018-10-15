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

    def generate(self, node=None, daughters=None, horizon=None):
        if node is None and daughters is None and horizon is None:
            node = self.root
            self.expand(node, self.branching_factor)
            self.generate(daughters=node.daughters, horizon=self.horizon)
        else:
            for daughter in daughters:
                if horizon is 2:
                    break
                # non-uniform branching factor after root expansion
                b_factor = self.branching_factor + random.randint(-1, 3)
                self.generate(daughters=self.expand(daughter, b_factor), horizon=horizon-1)

    @staticmethod
    def expand(node, branching_factor):
        for i in range(0, branching_factor):
            node.daughters.append(Node(random.randint(1, 101), node))
            node.daughters[i].depth = node.depth + 1
        return node.daughters

    def display(self, node=None, daughters=None):
        if node is None and daughters is None:
            node = self.root
            print(node.data)
            self.display(daughters=node.daughters)
        else:
            for daughter in daughters:
                for i in range(0, daughter.depth):
                    print("\t", end='', flush=True)
                print(daughter.data)
                if daughter.is_leaf() is False:
                    self.display(daughters=daughter.daughters)

    def export(self, filename, node=None, daughters=None, file=None):
        if file is None:
            file = open(filename, "w+")
            self.export(filename, node, daughters, file)
        else:
            if node is None and daughters is None:
                node = self.root
                file.write(str(node.data) + "\n")
                self.export(filename, daughters=node.daughters, file=file)
            else:
                for daughter in daughters:
                    for i in range(0, daughter.depth):
                        file.write("\t")
                    file.write(str(daughter.data) + "\n")
                    if daughter.is_leaf() is False:
                        self.export(filename, daughters=daughter.daughters, file=file)