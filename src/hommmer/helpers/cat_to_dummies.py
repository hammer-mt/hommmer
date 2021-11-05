import pandas as pd

def cat_to_dummies(df, columns):
    return pd.get_dummies(df, columns=columns)