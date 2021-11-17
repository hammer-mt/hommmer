import pandas as pd

def start_of_month(df, date_col):
    start_of_month = (df[date_col].dt.floor('d') + pd.offsets.MonthEnd(0) - pd.offsets.MonthBegin(1))
    df['start_of_month'] = start_of_month