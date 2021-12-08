def shift_dummies(df, col, shift):
    shift_cols = []
    shift_sign = "+"
    if shift < 0:
        shift_sign = "-"

    for t in range(shift):
        col_name = f"{col} t{shift_sign}{abs(t)}"
        df[col_name] = df[col].shift(t)
        shift_cols.append(col_name)
    
    if shift_sign == "+":
        prefix = "post"
    else:
        prefix = "pre"

    col_name = f"{prefix}-{col} {shift_sign}{abs(t)}"
    df[col_name] = (df[shift_cols].sum(axis=1) > 0).astype(int)
    shift_cols.push(col_name)
    return shift_cols