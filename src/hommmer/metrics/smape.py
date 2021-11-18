import numpy as np

def smape(y_actual, y_pred):
    # symmetric mean absolute percentage error
    return 100/len(y_actual) * np.sum(2 * np.abs(y_pred - y_actual) / (np.abs(y_actual) + np.abs(y_pred)))