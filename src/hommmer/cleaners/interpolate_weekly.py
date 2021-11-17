import numpy as np
import pandas as pd
import datetime as dt

def interpolate_weekly(df, date_col=None, resample_col=None):
    
    if date_col == None:
        date_col = df.columns[0]
        
    if resample_col == None:
        resample_col = df.columns[1]

    data = df[[date_col, resample_col]].copy()
        
    data[date_col] = data[date_col].apply(lambda x: dt.datetime.strptime(f"{x}-1", "%Y-%W-%w")) # mondays
    data[date_col] = pd.to_datetime(data[date_col]) # datetime
    data.set_index(date_col, inplace=True)
    data_reindexed = data.reindex(pd.date_range(start=data.index.min(),
                                        end=data.index.max() + dt.timedelta(days=6),
                                        freq='1D'))

    col_to_resample = data_reindexed.columns[0]
    data_reindexed[col_to_resample] = pd.to_numeric(data_reindexed[col_to_resample])
    data_reindexed[col_to_resample].replace({0:np.nan}, inplace=True)
    interpolated = data_reindexed.interpolate(method='linear')
    interpolated = interpolated / 7
    interpolated.reset_index(inplace=True)
    interpolated.rename({'index': 'date'}, axis=1, inplace=True)
    
    return interpolated