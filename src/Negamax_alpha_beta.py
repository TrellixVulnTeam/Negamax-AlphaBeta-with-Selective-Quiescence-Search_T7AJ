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

    def negamax(self, node, height):                        # STANDARD NEGAMAX ALGORITHM
        # if height is 0 or no moves possible from node
        if height is 0 or len(node.daughters) == 0:
            return self.evaluate(node)
        else:
            score = -10000
            for move in node.daughters:
                temp = -self.negamax(move, height-1)
                score = max(score, temp)
            return score

    def alphabeta(self, node, height, alpha, beta):         # ALPHA BETA NEGAMAX ALGORITHM
        # if height is 0 or no moves possible from node
        if height is 0 or len(node.daughters) == 0:
            return self.evaluate(node)
        else:
            for move in node.daughters:
                temp = -self.alphabeta(move, height-1, -beta, -alpha)
                if temp >= beta:        # beta cut-off
                    return temp
                alpha = max(temp, alpha)
            return alpha

    def selective_quiescence(self, node, alpha, beta):
        score = self.evaluate(node)
        if score >= beta:
            return score
        else:
            for move in node.daughters:
                if move.is_interesting:
                    temp = -self.selective_quiescence(move, -beta, -alpha)
                    if temp > score:
                        score = temp
                    if score >= alpha:
                        alpha = score
                    if score >= beta:
                        break
            return score

    def alphabeta_quiet(self, node, height, alpha, beta, maxing=True):
        # if height is 0 or no moves possible from node
        if height is 0 or len(node.daughters) == 0:
            if maxing is True:
                return self.selective_quiescence(node, alpha, beta)
            else:
                return self.selective_quiescence(node, -beta, alpha)
        else:
            for move in node.daughters:
                temp = -self.alphabeta_quiet(move, height-1, -beta, -alpha, not maxing)
                if temp >= beta:        # beta cut-off
                    return temp
                alpha = max(temp, alpha)
            return alpha
