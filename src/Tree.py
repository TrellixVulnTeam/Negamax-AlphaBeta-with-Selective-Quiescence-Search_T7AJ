"""
Name: Sabeer Bakir
Student No.: 16333886
Email: sabeer.bakir@ucdconnect.ie
"""


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
        :param i:   interesting threshold value
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
                b_factor = self.varying_branching_factor()
                if b_factor < 0:
                    b_factor = 0
                self.generate(daughters=self.expand(daughter, b_factor), horizon=horizon-1)

        nodelist = self.get_nodelist()
        for node in nodelist:
            if node.is_internal() and node.is_root() is False:  # Smudge evaluation results
                node.static_evaluation_val += random.randint(-self.approx, self.approx + 1)
            # checking if interesting
            if node.is_internal():
                node.is_interesting = (node.interesting < self.interestingness +
                                       (self.horizon - node.depth)*30)
            if node.is_leaf():
                if not (node.interesting < self.interestingness):
                    pass
                else:
                    node.is_interesting = True
                    nodelist += self.expand(node, self.varying_branching_factor(),
                                            self.interestingness - 2)
            if node.interesting is 10000:  # Never interesting
                node.interesting.interesting = 0
                node.is_interesting = False

    @classmethod    # TODO: FINISH WHEN REST IS OVER
    def from_file(cls, filename):   # For importing previously made trees
        file = open(filename, "r")
        line_number = 0
        for line in file:
            if line_number is 0:
                cls.root = Node(int(line.strip()), None)
                line_number += 1
            else:
                static_evaluation_val = int(line.strip())
                depth = line.count("\t")
                print(str(static_evaluation_val) + "\t" + str(depth))
                line_number += 1
        return cls(0, 0, cls.root.static_evaluation_val, 0, 0)

    def expand(self, node, branching_factor, interesting_threshold=0):
        if branching_factor > 0 or node.static_evaluation_val is not 10000:
            x = random.randint(0, 11)   # number from 1 - 10
            add_neg_parent = False

            for i in range(branching_factor):
                # 40% chance of occurring
                if (x <= 4 or i is (branching_factor - 1)) and add_neg_parent is False:
                    # negative of parent node
                    node.daughters.append(Node(-node.static_evaluation_val, node,
                                               interesting_threshold))
                    add_neg_parent = True
                else:
                    node.daughters.append(Node(random.randint(-node.static_evaluation_val, 10000),
                                               node, interesting_threshold))
            return node.daughters
        else:
            siblings = node.siblings()
            if len(siblings) < 2:
                return None     # Nothing left
            else:
                for sibling in siblings:
                    if sibling is not node:
                        b_factor = self.varying_branching_factor()
                        return self.expand(sibling, b_factor)

    def display(self, node=None, daughters=None):
        if node is None and daughters is None:
            node = self.root
            print(node.static_evaluation_val)
            # print(node.is_interesting)
            self.display(daughters=node.daughters)
        else:
            for daughter in daughters:
                for i in range(daughter.depth):
                    print("\t", end='', flush=True)
                print(daughter.static_evaluation_val)
                # print(daughter.is_interesting)
                if daughter.is_leaf() is False:
                    self.display(daughters=daughter.daughters)

    def export(self, filename, node=None, daughters=None, file=None):
        if file is None:
            file = open(filename, "w+")
            self.export(filename, node, daughters, file)
        else:
            if node is None and daughters is None:
                node = self.root
                file.write(str(node.static_evaluation_val) + "\n")
                self.export(filename, daughters=node.daughters, file=file)
            else:
                for daughter in daughters:
                    for i in range(daughter.depth):
                        file.write("\t")
                    file.write(str(daughter.static_evaluation_val) + "\n")
                    if daughter.is_leaf() is False:
                        self.export(filename, daughters=daughter.daughters, file=file)

    def get_nodelist(self, node=None, nodelist=None):  # Get list of nodes from 'node' downwards
        if node is None and nodelist is None:
            nodelist = []
            node = self.root
            nodelist.append(node)
            for node in node.daughters:
                self.get_nodelist(node, nodelist)
        else:
            nodelist.append(node)
            for node in node.daughters:
                self.get_nodelist(node, nodelist)

        return nodelist

    def varying_branching_factor(self):
        b_factor = self.branching_factor
        chance = random.randint(1, 101)  # this number is to help vary branching factor
        if chance in range(1, 4):  # 3% chance
            b_factor = self.branching_factor + 2
        elif chance in range(4, 10):  # 6% chance
            b_factor = self.branching_factor + 1
        elif chance in range(10, 90):  # 80% chance
            b_factor = self.branching_factor
        elif chance in range(90, 97):  # 7% chance
            b_factor = self.branching_factor - 1
        elif chance in range(97, 101):  # 4% chance
            b_factor = self.branching_factor - 2
        return b_factor
