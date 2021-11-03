import numpy as np
from sklearn import metrics

def rmse(y_actual, y_pred):
    # root mean square error
    return round(np.sqrt(metrics.mean_squared_error(y_actual, y_pred)), 3)