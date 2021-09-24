import pandas as pd
import statsmodels.api as sm

def model(df, y_label, X_labels, constant=True):
    keep_columns = [y_label] + X_labels
    df_copy = df[keep_columns].copy()
    X = sm.add_constant(df_copy.drop(y_label, axis=1))
    y = df[y_label]
    est = sm.OLS(y, X).fit()
    print(est.summary())