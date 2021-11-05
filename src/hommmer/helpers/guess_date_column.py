def guess_date_column(columns):
    columns = [x.lower() for x in columns]
    guesses = ['date', 'day', 'week', 'month']
    for x in guesses:
        if x in columns:
            return x
    return None