def count_na_cols(df):
    missing = df.isna().sum() * 100 / len(df)
    return missing[missing > 0].sort_values(ascending=False)