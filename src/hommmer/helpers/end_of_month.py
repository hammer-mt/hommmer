import pandas as pd

def end_of_month(df, date_col):
    end_of_month = pd.to_datetime(df[date_col]) + pd.offsets.MonthEnd(1)
    df['end_of_month'] = end_of_month
