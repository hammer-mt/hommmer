import pandas as pd
import datetime as dt

def search_trends(df):
    # delete any '<' signs for low volume days
    for c in df.select_dtypes(include=['object']).columns[1:]:
        df[c] = df[c].str.replace('<', '')
        df[c] = pd.to_numeric(df[c])

    date_col = df.columns[0]
    df[date_col] = pd.to_datetime(df[date_col])
    df.set_index(date_col, inplace=True)
    df_reindexed = df.reindex(pd.date_range(start=df.index.min(),
                                            end=df.index.max() + dt.timedelta(days=6), freq='1D'))
    df = df_reindexed.interpolate(method='linear')
    df = df.round(1)
    df.reset_index(inplace=True)
    df.rename({'index': 'date'}, axis=1, inplace=True)
    return df