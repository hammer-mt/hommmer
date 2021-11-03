def rename_column(df, column_label, new_name):
    df.rename(columns={column_label: new_name}, inplace=True)