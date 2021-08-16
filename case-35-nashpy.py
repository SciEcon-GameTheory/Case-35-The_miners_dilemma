import numpy as np
import nashpy as nash

pool2 = np.array([[1, 0],
              [2, 0.5]])

pool1 = np.array([[1, 2],
              [0, 0.5]])

game = nash.Game(pool2, pool1)

equilibria = game.support_enumeration()
for eq in equilibria:
  print(eq)