import numpy as np
import pandas as pd

def interpolate_dates(df, date_col=None):
    data = df.copy()
    if date_col is None:
        date_col = data.columns[0]

    data[date_col] = pd.to_datetime(data[date_col])

    dr = pd.date_range(start=data[date_col].min(), end=data[date_col].max(), freq='1D')

    date_df = pd.DataFrame({f'{date_col}': dr})

    merged = date_df.merge(data, how='left', on=date_col)
    reindexed = merged.set_index(date_col)

    reindexed.replace({0: np.nan}, inplace=True)
    resampled = reindexed.interpolate(method='linear')
    resampled = resampled.reset_index()
    resampled.rename({'index': date_col}, axis=1, inplace=True)
    resampled.fillna(0, inplace=True)
    return resampled