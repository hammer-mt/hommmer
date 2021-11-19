import numpy as np

def dummy_constant(y_actual, constant):
    # dummy constant predictor
    return np.full(y_actual.shape, constant)