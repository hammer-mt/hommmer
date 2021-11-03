import pandas as pd

def date_range_dummies(df):
    dr = pd.date_range(start=df['start'].min(), end=df['end'].max())
    
    date_df = pd.DataFrame({'date': dr})

    for _, row in df.iterrows():
        date_df[row[2]] = (date_df['date'] >= row[0]) & (date_df['date'] <= row[1])
        
    date_df.iloc[:, 1:] = date_df.iloc[:, 1:].astype(int)
    return date_df