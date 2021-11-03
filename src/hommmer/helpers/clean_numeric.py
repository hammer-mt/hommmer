import pandas as pd

def clean_numeric(series):
    series = series.fillna(0)
    series = series.astype(str)
    series = series.apply(lambda x: x.replace(',',''))
    series = series.apply(lambda x: x.replace('$',''))
    series = series.apply(lambda x: x.replace('£',''))
    series = series.apply(lambda x: x.replace('€',''))
    series = pd.to_numeric(series)

    return series