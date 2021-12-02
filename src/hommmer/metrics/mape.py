from sklearn import metrics
import numpy as np

def mape(y_actual, y_pred):
    # mean absolute percentage error
    value = round(metrics.mean_absolute_error(y_actual, y_pred)/np.mean(y_actual),3)
    passed = "✔️" if value < 0.15 else "❌"
    return value, passed