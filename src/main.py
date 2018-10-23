"""
Name: Sabeer Bakir
Student No.: 16333886
Email: sabeer.bakir@ucdconnect.ie
"""


from Tree import Tree
import random
from Negamax_alpha_beta import Negamax

random_val = random.randint(-2500, 2501)
negamax = Negamax()


print("1) Generate Tree ?")
print("2) Import Tree ? ")
try:
    choice = int(input("Input: "))
    if choice is 1:
        b = int(input("Branching Factor: "))
        h = int(input("Horizon: "))
        v = random_val
        approx = int(input("Value Smudging Factor: "))
        i = int(input("Interesting Threshold: "))
        tree = Tree(b, h, v, approx, i)
        tree.generate()
    elif choice is 2:
        filename = input("Filename: ")
        try:
            file = open(filename, "r")
            tree = Tree.from_file(file)
        except FileNotFoundError:
            print("File Does Not Exist")
            exit()
    else:
        print("Invalid Option")
        exit()
except ValueError:
    print("Please Enter Integer Values Only")
    exit()

run = True  # for while loop
while run:
    print("1) Display Tree")
    print("2) Export Tree")
    print("3) Negamax Search")
    print("4) Negamax Alpha Beta Search")
    print("5) Selective Quiescence Search")
    print("6) Exit")

    try:
        choice = int(input("Input: "))
        if choice is 1:
            tree.display()
            print()
        elif choice is 2:
            filename = input("Export Filename: ")
            tree.export(filename)
            print("Export Complete!")
        elif choice is 3:
            score = negamax.negamax(tree.root, tree.root.height)
            print("NEGAMAX SEARCH ALGORITHM")
            print("Score: " + str(score))
            print("Evaluations: " + str(negamax.evaluations))
            negamax.evaluations = 0     # reset for future searches
        elif choice is 4:
            score = negamax.alphabeta(tree.root, tree.root.height, negamax.alpha, negamax.beta)
            print("NEGAMAX ALPHA BETA SEARCH ALGORITHM")
            print("Score: " + str(score))
            print("Evaluations: " + str(negamax.evaluations))
            negamax.evaluations = 0     # reset for future searches
        elif choice is 5:
            score = negamax.selective_quiescence(tree.root, negamax.alpha, negamax.beta)
            print("SELECTIVE QUIESCENCE SEARCH ALGORITHM")
            print("Score: " + str(score))
            print("Evaluations: " + str(negamax.evaluations))
            negamax.evaluations = 0     # reset for future searches
        elif choice is 6:
            run = False
            exit()
        else:
            print("Invalid Option")
            exit()
    except ValueError:
        print("Please Enter Integer Values Only")
        exit()
    print()
