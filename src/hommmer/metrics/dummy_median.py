import numpy as np

def dummy_median(y_actual):
    # dummy median predictor
    return np.full(y_actual.shape, np.median(y_actual))