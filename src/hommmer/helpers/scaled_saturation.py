import numpy as np

def scaled_saturation(x, alpha=None):
    if alpha is None:
        alpha = x.max()
    return alpha * (1 - np.exp(x/-alpha))