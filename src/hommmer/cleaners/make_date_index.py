import pandas as pd

def make_date_index(df, date_label):
    df[date_label] = pd.to_datetime(df[date_label])
    df.index = df[date_label]
    df.drop(date_label, axis=1, inplace=True)
    df.index.name = None