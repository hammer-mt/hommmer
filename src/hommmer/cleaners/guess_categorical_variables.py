def guess_categorical_variables(df):
    cat_vars = []
    for x in df.columns:
        values = list(df[x].value_counts().index)
        if values in [[0, 1], [1], [True, False], [True]]:
            cat_vars.append(x)

    return cat_vars