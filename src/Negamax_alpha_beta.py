"""
Name: Sabeer Bakir
Student No.: 16333886
Email: sabeer.bakir@ucdconnect.ie
"""


class Negamax:
    def __init__(self):
        self.evaluations = 0
        self.alpha = -10000
        self.beta = 10000

    def evaluate(self, node):
        self.evaluations += 1
        return node.static_evaluation_val

    def search(self, node, height):
        # if height is 0 or no moves possible from node
        if height is 0 or len(node.daughters) == 0:
            return self.evaluate(node)
        else:
            temp = 0
            score = -10000
            for move in node.daughters:
                temp = -self.search(move, height-1)
                score = max(score, temp)
                print(score)
            return score
