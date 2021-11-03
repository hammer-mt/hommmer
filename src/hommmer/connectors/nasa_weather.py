import pandas as pd

def nasa_weather(df):
    year = df['YEAR'].astype(str)
    month = df['MO'].astype(str)
    day = df['DY'].astype(str)
    
    month = month.apply(lambda x: '0'+x if len(x) == 1 else x)
    day = day.apply(lambda x: '0'+x if len(x) == 1 else x)
    
    df['date'] = pd.to_datetime(year + "-" + month + "-" + day)
    df = df[['date', 'T2M_RANGE', 'T2M_MAX', 'T2M_MIN', 'T2M']]
    
    return df