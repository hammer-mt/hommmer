import numpy as np
import pandas as pd

def exp_ex_zeros(series):
    np_array = np.array(series.values, dtype=np.float)
    out = np.zeros_like(np_array)
    exponent = np.exp(np_array, where=np_array!=0, out=out)
    exp_series = pd.Series(exponent, name=series.name, index=series.index)
    return exp_series