from sklearn import metrics

def calculate_mae(y_actual, y_pred):
    # mean absolute error
    return round(metrics.mean_absolute_error(y_actual, y_pred),3)