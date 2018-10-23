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
        if len(self.root.daughters) is 0:
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

    @classmethod
    def from_file(cls, file):   # For importing previously made trees
        nodelist = []
        for line in file:
            values = cls.create_map(line)
            if line.startswith("b: "):
                b = int(values.get('b'))
                h = int(values.get('h'))
                v = int(values.get('v'))
                approx = int(values.get('approx'))
                i = int(values.get('i'))
            else:
                static_evaluation = int(values.get('static_evaluation'))
                if values.get('parent') == 'None':
                    parent = None
                else:
                    parent = int(values.get('parent'))
                daughters = cls.string_to_list(values.get('daughters'))
                depth = int(values.get('depth'))
                interesting = int(values.get('interesting'))
                is_interesting = cls.string_to_bool(values.get('is_interesting'))
                daughters_size = len(daughters)
                if parent is None:
                    cls.root = Node(static_evaluation, parent)
                    cls.root.interesting = interesting
                    cls.root.is_interesting = is_interesting
                    cls.root.daughters_size = daughters_size
                    nodelist = [cls.root]
                else:
                    for node in nodelist:
                        # print(node.static_evaluation_val)
                        # print(parent)
                        # print(node.daughters_size)
                        # print(len(node.daughters))
                        # print()
                        if node.static_evaluation_val == parent and \
                                not (node.daughters_size is len(node.daughters)) and \
                                (node.depth is depth - 1):
                            daughter = node.add_daughter(static_evaluation)
                            daughter.interesting = interesting
                            daughter.is_interesting = is_interesting
                            daughter.daughters_size = daughters_size
                            nodelist.append(daughter)

        return cls(b, h, v, approx, i)

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

    def export(self, filename):
        file = open(filename, "w+")
        nodelist = self.get_nodelist()
        file.write("b: " + str(self.branching_factor) + "\t" +
                   "h: " + str(self.horizon) + "\t" +
                   "v: " + str(self.root.static_evaluation_val) + "\t" +
                   "approx: " + str(self.approx) + "\t" +
                   "i: " + str(self.interestingness) + "\n")
        for node in nodelist:
            if node.is_root():
                file.write("static_evaluation: " + str(node.static_evaluation_val) + "\t" +
                           "parent: " + str(node.parent) + "\t" +
                           "daughters: " + str(node.daughters_val()) + "\t" +
                           "depth: " + str(node.depth) + "\t" +
                           "interesting: " + str(node.interesting) + "\t" +
                           "is_interesting: " + str(node.is_interesting) + "\t\n")
            else:
                file.write("static_evaluation: " + str(node.static_evaluation_val) + "\t" +
                           "parent: " + str(node.parent.static_evaluation_val) + "\t" +
                           "daughters: " + str(node.daughters_val()) + "\t" +
                           "depth: " + str(node.depth) + "\t" +
                           "interesting: " + str(node.interesting) + "\t" +
                           "is_interesting: " + str(node.is_interesting) + "\t\n")

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

    def get_nodelist_val(self, node=None, nodelist=None):
        if node is None and nodelist is None:
            nodelist = []
            node = self.root
            nodelist.append(node.static_evaluation_val)
            for node in node.daughters:
                self.get_nodelist(node, nodelist)
        else:
            nodelist.append(node.static_evaluation_val)
            for node in node.daughters:
                self.get_nodelist(node, nodelist)

        return nodelist

    @staticmethod
    def create_map(line):
        line = line.strip()
        split = line.split("\t")
        mapping = dict({})
        temp = []
        for item in split:
            temp.append(item.split(": "))
        for key in temp:
            mapping.update({key[0]: key[1]})
        return mapping

    @staticmethod
    def string_to_list(string):
        string = string.strip('[')
        string = string.strip(']')
        mylist = string.split(', ')
        int_list = []
        for item in mylist:
            if item is '':
                return int_list
            int_list.append(int(item))
        return int_list

    @staticmethod
    def string_to_bool(string):
        if string.strip() == 'True':
            return True
        else:
            return False
