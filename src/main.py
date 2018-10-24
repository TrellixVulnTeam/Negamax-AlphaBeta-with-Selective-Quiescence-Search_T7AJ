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
value_is_correct = False

print("1) Generate Tree ?")
print("2) Import Tree ? ")
print("3) Run Systematic Analysis (As per Assignment)")
# try:
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
elif choice is 3:
    file = open("Assignment 1.txt", "w+")
    interestingness = 20
    for b_factor in range(3, (11 ** 3) + 1, 4):
        for horizon in range(4, 7 + 1):
            for approx in range(100, 300 + 1, 100):
                for run_num in range(12):
                    file.write("----------------------------------------\n")
                    file.write("RUN NUMBER " + str(run_num + 1) + "\n")
                    file.write("----------------------------------------\n")
                    file.write("branching factor: " + str(b_factor) + "\n")
                    file.write("horizon: " + str(horizon) + "\n")
                    value = random.randint(-2500, 2501)
                    file.write("desired value: " + str(value) + "\n")
                    file.write("approx: " + str(approx) + "\n")
                    file.write("interestingness: " + str(interestingness) + "\n")
                    file.write("\n")
                    tree = Tree(b_factor, horizon, value, approx, interestingness)
                    tree.generate()
                    file.write("NEGAMAX ALPHA BETA SEARCH" + "\n")
                    file.write("Horizon-2: " + "\n")
                    file.write("Score: " + str(negamax.alphabeta(tree.root, horizon-2,
                                                                 negamax.alpha, negamax.beta))
                               + "\n")
                    file.write("Evaluations: " + str(negamax.evaluations) + "\n")
                    negamax.evaluations = 0     # reset evaluations
                    file.write("\n")
                    file.write("Horizon-1: " + "\n")
                    file.write("Score: " + str(negamax.alphabeta(tree.root, horizon-1,
                                                                 negamax.alpha, negamax.beta))
                               + "\n")
                    file.write("Evaluations: " + str(negamax.evaluations) + "\n")
                    negamax.evaluations = 0     # reset evaluations
                    file.write("\n")
                    file.write("Horizon: " + "\n")
                    file.write("Score: " + str(negamax.alphabeta(tree.root, horizon,
                                                                 negamax.alpha, negamax.beta))
                               + "\n")
                    file.write("Evaluations: " + str(negamax.evaluations) + "\n")
                    negamax.evaluations = 0     # reset evaluations
                    file.write("\n")
                    file.write("SELECTIVE QUIESCENCE SEARCH" + "\n")
                    file.write("Score: " + str(negamax.selective_quiescence(tree.root,
                                                                            negamax.alpha,
                                                                            negamax.beta))
                               + "\n")
#     else:
#         print("Invalid Option")
#         exit()
# except ValueError:
#     print("Please Enter Integer Values Only")
#     exit()

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
            print("NEGAMAX SEARCH ALGORITHM")
            print()
            height = tree.root.height
            while not value_is_correct:
                try:
                    height = int(input("Enter height (Enter 0 for height of root): "))
                    if height is 0:
                        height = tree.root.height
                    if height < 0 or height > tree.root.height:
                        print("Enter values between 0 and " + str(tree.root.height) + " Inclusive")
                    else:
                        value_is_correct = True
                except ValueError:
                    print("Enter Valid Integer Value")
            print()
            score = negamax.negamax(tree.root, height)
            print("Score: " + str(score))
            print("Evaluations: " + str(negamax.evaluations))
            negamax.evaluations = 0     # reset for future searches
            value_is_correct = False    # reset for future searches
        elif choice is 4:
            print("NEGAMAX ALPHA BETA SEARCH ALGORITHM")
            print()
            height = tree.root.height
            while not value_is_correct:
                try:
                    height = int(input("Enter height (Enter 0 for height of root): "))
                    if height is 0:
                        height = tree.root.height
                    if height < 0 or height > tree.root.height:
                        print("Enter values between 0 and " + str(tree.root.height) + " Inclusive")
                    else:
                        value_is_correct = True
                except ValueError:
                    print("Enter Valid Integer Value")
            print()
            score = negamax.alphabeta(tree.root, height, negamax.alpha, negamax.beta)
            print("Score: " + str(score))
            print("Evaluations: " + str(negamax.evaluations))
            negamax.evaluations = 0     # reset for future searches
        elif choice is 5:
            print("SELECTIVE QUIESCENCE SEARCH ALGORITHM")
            print()
            score = negamax.selective_quiescence(tree.root, negamax.alpha, negamax.beta)
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
