import datetime as dt

def week_commencing(date_str=None, date_format="%Y-%m-%d"):
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

    # if no date supplied, default to today
    if date_str is None:
        today = dt.datetime.today()
        date_str = today.strftime(date_format)

    # parse the date string into a datetime object
    date = dt.datetime.strptime(date_str, date_format)

    # get the year and week number from the datetime
    year_week = dt.datetime.strftime(date, "%Y-%W")

    # hack to get the monday of the week
    monday = dt.datetime.strptime(f"{year_week}-1", "%Y-%W-%w")

    # return the monday date in the same format
    return dt.datetime.strptime(monday, date_format)