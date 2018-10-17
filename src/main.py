"""
Name: Sabeer Bakir
Student No.: 16333886
Email: sabeer.bakir@ucdconnect.ie
"""


from Tree import Tree
import random

# tree = Tree(2, 4, 40, 0, 0)
# tree.generate()
# tree = Tree.from_file("tree.txt")
# tree.display()
# tree.export("tree.txt")

random_val = random.randint(-2500, 2501)

tree = Tree(2, 5, random_val, 20, 0)
tree.generate()
tree.display()
tree.export("tree.txt")
