import datetime as dt
import pandas as pd

def make_dates(days=180, end_date=None):
    if end_date:
        end_date = dt.datetime.strptime(end_date, "%Y-%m-%d")
    else:
        end_date =  dt.datetime.today()

    start_date = end_date - dt.timedelta(days-1)
    dates = pd.date_range(start_date, periods=days, freq='D')
    dates = pd.Series(dates.strftime("%Y-%m-%d"))
    return dates