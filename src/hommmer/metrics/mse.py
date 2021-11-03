from sklearn import metrics

def mse(y_actual, y_pred):
    # mean square error
    return round(metrics.mean_squared_error(y_actual, y_pred), 3)