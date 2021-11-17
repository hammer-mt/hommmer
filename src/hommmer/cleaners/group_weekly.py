def group_weekly(df, date_col):
    weekly = df.copy()
    weekly['week'] = weekly[date_col].dt.isocalendar().week
    weekly['year'] = weekly[date_col].dt.isocalendar().year
    weekly['year_week'] = weekly['year'].astype(str) + "-" + weekly['week'].astype(str)
    weekly = weekly.groupby('year_week').sum()
    weekly.drop(['week', 'year'], axis=1, inplace=True)
    weekly.reset_index(inplace=True)
    return weekly