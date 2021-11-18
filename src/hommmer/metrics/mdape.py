import numpy as np

def mdape(y_actual, y_pred):
    # median absolute percentage error
    return np.median(np.abs((y_actual - y_pred) / y_actual)) * 100