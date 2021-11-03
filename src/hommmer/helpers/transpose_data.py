def transpose_data(df, date_col=None):
    if date_col is None:
        date_col = df.columns[0]

    transposed = df.T.copy()
    transposed.columns = transposed.iloc[0]
    transposed.drop(transposed.index[0], inplace=True)
    transposed.reset_index(inplace=True)
    transposed.rename(columns={"index": date_col}, inplace=True)
    transposed = transposed.rename_axis(None, axis = 1)
    return transposed