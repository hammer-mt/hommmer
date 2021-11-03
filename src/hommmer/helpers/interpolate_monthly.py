import numpy as np
import pandas as pd

def interpolate_monthly(df, date_col=None, resample_col=None):
    
    if date_col == None:
        date_col = df.columns[0]
        
    if resample_col == None:
        resample_col = df.columns[1]

    data = df[[date_col, resample_col]].copy()

    data[date_col] = pd.to_datetime(data[date_col], format="%Y-%m")
    data['start_of_month'] = (data[date_col].dt.floor('d') + pd.offsets.MonthEnd(0) - pd.offsets.MonthBegin(1))
    data['end_of_month'] = pd.to_datetime(data['start_of_month']) + pd.offsets.MonthEnd(1)
    data['days_in_month'] = (data['end_of_month'] - data['start_of_month']).dt.days + 1
    data[resample_col] = data[resample_col] / data['days_in_month']
    reindexed = data.set_index("start_of_month")
    reindexed = reindexed.reindex(pd.date_range(start=reindexed.index.min(),
                                        end=reindexed.end_of_month.max(),
                                        freq='1D'))
    
    resampled = reindexed[resample_col]
    resampled.replace({0:np.nan}, inplace=True)
    resampled = resampled.interpolate(method='linear')
    resampled = resampled.reset_index()
    resampled.rename({'index': 'date'}, axis=1, inplace=True)
    resampled.fillna(0, inplace=True)
    return resampled