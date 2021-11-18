from sklearn import metrics
import numpy as np
# https://github.com/CamDavidsonPilon/Python-Numerics/blob/master/TimeSeries/MASE.py
# https://medium.com/@ashishdce/mean-absolute-scaled-error-mase-in-forecasting-8f3aecc21968

def mase(y_train, y_test, y_pred):
    # mean absolute scaled error
    n = y_train.shape[0]
    naive = np.abs(np.diff(y_train).sum()/(n-1))
    mae = metrics.mean_absolute_error(y_test, y_pred)

    return round(mae/naive,3)