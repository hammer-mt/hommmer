import numpy as np
import scipy.optimize as sco

from .loss_function import loss_function

def optimizer(X_media, X_org, budget):
    args = (X_media, X_org) # pass non-optimized values into model_function
    len_X_media = len(X_media['labels'])
    guesses = len_X_media*[budget/len_X_media,] # starting guesses: divide budget evenly
    con_1 = {'type': 'eq', 'fun': lambda X: np.sum(X) - budget} # so we can't go over budget
    constraints = (con_1)
    bound = (0, budget) # spend for a channel can't be negative or higher than budget
    bounds = tuple(bound for x in range(len_X_media))
    solution = sco.minimize(loss_function, x0=guesses, args=args, method='SLSQP', constraints=constraints, bounds=bounds)
    return (-1 * solution.fun), solution.x