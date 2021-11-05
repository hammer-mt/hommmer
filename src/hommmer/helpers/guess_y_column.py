def guess_y_column(columns):
    guesses = ['revenue', 'sales', 'conversions', 'purchases']
    columns = [x.lower() for x in columns]
    for x in guesses:
        if x in columns:
            return x
    return None
