import pandas as pd

def merge_data(left_df, right_df, date_col="date"):

    # get clean copies of data with date format
    left_df = left_df.copy()
    left_df['date'] = pd.to_datetime(left_df['date'])

    right_df = right_df.copy()
    right_df['date'] = pd.to_datetime(right_df['date'])

    # join data together
    merged_df = left_df.merge(right_df, on=date_col, how='left')
    merged_df.fillna(0, inplace=True)
    return merged_df