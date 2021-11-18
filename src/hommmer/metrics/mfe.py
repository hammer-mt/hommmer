import numpy as np
# https://datasciencestunt.com/mean-directional-accuracy-of-time-series-forecast/

def mfe(y_actual, y_pred):
    # mean forecast error or forecast bias
    return np.mean(y_actual - y_pred)