import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from typing import List

from .helpers import bfe
from .helpers import nrsme

def model(df:pd.DataFrame, date_label:str, y_label:str, X_labels:List[str]) -> None:
    """Builds a Marketing Mix Model
    Params:
    - df: Pandas DataFrame - contains your data (weekly Mon->Sun)
    - date_label: str - the date (YYYY-MM-DD) at the start of the week (Mon)
    - y_label: str - the dependent variable or target (sales, revenue, leads, etc)
    - X_labels: List[str] - a list of explanatory variables (media spend, seasonality, etc)
    
    Results:
    - prints model
    - displays charts
    """
    # keep only the columns we need
    keep_columns = [y_label, date_label] + X_labels

    # make a copy of the dataframe so we don't change the original
    model_df = df[keep_columns].copy()

    # split out the X_data and y_data
    y_data = model_df[y_label]
    X_data = model_df[X_labels]

    # add a constant to the X_data
    X_data = sm.add_constant(X_data)

    # generate train test splits
    X_train, X_test, y_train, y_test = train_test_split(X_data, y_data,
        test_size=0.2, random_state=1130)

    # run backwards feature elimination (BFE) to get only important features
    important_features = bfe(y_train, X_train)

    # run model with only important_features
    X_train_if = X_train[important_features]
    est = sm.OLS(y_train, X_train_if).fit()

    # predict y_test with model
    X_test_if = X_test[important_features]
    y_pred = est.predict(X_test_if)

    # get model coefficients and p_values
    coefs = est.params.values
    p_values = est.p_values.values

    # get the normalized root mean square error
    nrmse = nrsme(y_test, y_pred)

    print(est.summary())