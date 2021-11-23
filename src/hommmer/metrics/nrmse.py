import numpy as np
from sklearn import metrics

def nrmse(y_actual, y_pred):
    # normalized root mean square error
    value = round(np.sqrt(metrics.mean_squared_error(y_actual, y_pred)) / np.mean(y_actual), 3)
    passed = "✔️" if value < 0.15 else "❌"
    return value, passed