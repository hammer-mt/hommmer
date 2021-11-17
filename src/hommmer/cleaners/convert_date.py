import datetime as dt

def convert_date(date, from_format="%m/%d/%Y", to_format="%Y-%m-%d"):
    date_str = str(date)
    date_obj = dt.datetime.strptime(date_str, from_format)
    return dt.datetime.strftime(date_obj, to_format)