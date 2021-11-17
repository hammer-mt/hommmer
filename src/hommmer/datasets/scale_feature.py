
import numpy as np

def scale_feature(series, min_value=None, max_value=None):
    # if no min or max values supplied
    if min_value is None:
        min_value = 0
    if max_value is None:
        max_value = series.max() * 100
        
    return np.interp(series, (series.min(), series.max()), (min_value, max_value))