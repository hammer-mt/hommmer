import numpy as np
# https://datasciencestunt.com/mean-directional-accuracy-of-time-series-forecast/

def mda(y_actual, y_pred):
    # mean directional accuracy
    return np.mean((np.sign(y_actual[1:] - y_actual[:-1]) == np.sign(y_pred[1:] - y_pred[:-1])).astype(int))