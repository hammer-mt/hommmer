import numpy as np

def remove_outliers(series, num_std_devs=3):
    mean = np.mean(series)
    std_dev = np.std(series)
    outliers_cutoff = std_dev * num_std_devs
    lower_limit = mean - outliers_cutoff
    upper_limit = mean + outliers_cutoff

    no_outliers = series.apply(lambda x: mean if x > upper_limit or x < lower_limit else x)

    return no_outliers