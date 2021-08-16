import quantecon.game_theory as gt
import numpy as np

dilemma_matrix = np.array([[(1, 1), (0, 2)],
                           [(2, 0), (0.5, 0.5)]])

g_MD = gt.NormalFormGame(dilemma_matrix)

NE = gt.support_enumeration(g_MD)

print(NE)