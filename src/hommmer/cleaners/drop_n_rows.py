def drop_n_rows(df, n=1, top=False):
    if top:
        df.drop(df.head(n).index, inplace=True) # drop first n rows
    else:
        df.drop(df.tail(n).index, inplace=True) # drop last n rows