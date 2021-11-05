def count_dup_cols(df):
    duplicate = df.duplicated().sum() * 100 / len(df)
    return duplicate[duplicate > 0].sort_values(ascending=False)