from hommmer.metrics import *

def check_metric(metric_label, y_train, y_pred):
    return {
        'nrmse': nrmse(y_train, y_pred),
        'rsquared': rsquared(y_train, y_pred)
    }[metric_label]