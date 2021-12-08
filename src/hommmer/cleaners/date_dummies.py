import pandas as pd

def date_dummies(df):
    dr = pd.date_range(start=df['date'].min(), end=df['date'].max())
    date_df = pd.DataFrame({'date': dr})
    for _, row in df.iterrows():
        date_df[row[1]] = (date_df['date'] == row[0])
        
    date_df.iloc[:, 1:] = date_df.iloc[:, 1:].astype(int)
    return date_df