import numpy as np
import pandas as pd

def log_ex_zeros(series):
    np_array = np.array(series.values, dtype=np.float)
    out = np.zeros_like(np_array)
    logged = np.log(np_array, where=np_array!=0, out=out)
    log_series = pd.Series(logged, name=series.name, index=series.index)
    return log_series