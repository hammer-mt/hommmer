def make_column_index(df, column_label):
    df.index = df[column_label]
    df.drop(column_label, axis=1, inplace=True)
    df.index.name = None