def group_monthly(df, date_col):
    monthly = df.copy()
    monthly['month'] = monthly[date_col].dt.month
    monthly['year'] = monthly[date_col].dt.isocalendar().year
    monthly['year_month'] = monthly['year'].astype(str) + "-" + monthly['month'].astype(str)
    monthly = monthly.groupby('year_month').sum()
    monthly.drop(['month', 'year'], axis=1, inplace=True)
    monthly.reset_index(inplace=True)
    return monthly