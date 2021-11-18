import numpy as np

def dummy_mean(y_actual):
    # dummy mean predictor
    return np.full(y_actual.shape, np.mean(y_actual))
    