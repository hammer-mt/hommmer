from sklearn import metrics

def rsquared(y_actual, y_pred):
    # r squared
    return round(metrics.r2_score(y_actual, y_pred), 3)