def drop_cols(df, columns):
    df.drop(columns, axis=1, inplace=True)