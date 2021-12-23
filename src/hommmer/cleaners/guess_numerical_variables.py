import numpy as np

def guess_numerical_variables(df):
    return list(df.select_dtypes(include=[np.number]).columns.values)