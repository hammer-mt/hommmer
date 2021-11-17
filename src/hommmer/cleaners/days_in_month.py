import pandas as pd

def days_in_month(df, date_col):
    start_of_month = (df[date_col].dt.floor('d') + pd.offsets.MonthEnd(0) - pd.offsets.MonthBegin(1))
    end_of_month = pd.to_datetime(df[date_col]) + pd.offsets.MonthEnd(1)
    df['days_in_month'] = (end_of_month - start_of_month).dt.days + 1