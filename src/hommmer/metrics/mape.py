from sklearn import metrics

def calculate_mape(y_actual, y_pred):
    # mean absolute percentage error
    return round(metrics.mean_absolute_percentage_error(y_actual, y_pred), 3)