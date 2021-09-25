import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from typing import List

from .helpers import bfe

def model(df:pd.DataFrame, date_label:str, y_label:str, X_labels:List[str]) -> None:
    """Builds a Marketing Mix Model
    Params:
    - df: Pandas DataFrame - contains your data
    - date_label: str - the date column (YYYY-MM-DD)
    - y_label: str - the dependent variable
    - X_labels: List[str] - a list of explanatory variables
    
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

    # run backwards feature elimination (BFE) to get only significant variables
    important_features = bfe(y_train, X_train)

    est = sm.OLS(y_train, X_train).fit()
    print(est.summary())