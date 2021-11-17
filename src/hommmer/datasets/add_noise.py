import numpy as np

def add_noise(series):
    series = np.array(series)
    series += np.random.normal(scale=0.1, size=series.shape)
    series = np.squeeze(series)
    return series