import numpy as np
import pandas as pd

def unstack_data(df, metric_column, unstack_column, date_column='date'):

    # make a copy of the date with just the columns we need
    data = df[[date_column, metric_column, unstack_column]].copy()

    # convert the metric column to numeric
    data[metric_column] = pd.to_numeric(data[metric_column])

    # pivot the data set
    pivoted = pd.pivot_table(data, index=[date_column], values=[metric_column], columns=[unstack_column], aggfunc=[np.sum])
    
    # drop level and reset index
    pivoted.columns = pivoted.columns.droplevel(0)
    pivoted.columns.name = None
    pivoted = pivoted.reset_index()
    pivoted.columns = [col[1] for col in pivoted.columns]

    # rename unstacked metric columns
    metric_columns = list(pivoted.columns[1:])
    metric_columns = [f"{c} | {metric_column}" for c in metric_columns]
    pivoted.columns = [date_column] + metric_columns

    # replace errors with zeros
    pivoted.fillna(0, inplace=True)

    # return the pivoted data
    return pivoted