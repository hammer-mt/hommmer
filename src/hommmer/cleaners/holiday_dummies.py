import re
import pandas as pd

from hommmer.datasets import load_holidays

def holiday_dummies(start, end, country="US", brackets=False):
    all_holidays = load_holidays(download=False)
    country_holidays = all_holidays[all_holidays['country'] == country]
    if brackets == False:
        country_holidays['holiday'] = country_holidays['holiday'].apply(
            lambda x: re.sub(' [\[\(].*[\]\)]','', x))
    
    dr = pd.date_range(start=start, end=end)
    date_df = pd.DataFrame({'ds': dr})
    for _, row in country_holidays.iterrows():
        if row[1] in date_df.columns:
            date_df[row[1]] = date_df[row[1]] | (date_df['ds'] == row[0])
        else:
            date_df[row[1]] = (date_df['ds'] == row[0])

    date_df.iloc[:, 1:] = date_df.iloc[:, 1:].astype(int)
    return date_df

