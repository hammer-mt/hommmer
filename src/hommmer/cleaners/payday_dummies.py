def add_payday_dummies(df, date_label):
    payday_column = 'payday'
    df[payday_column] = df[date_label].apply(lambda x:1 if x.strftime('%d') in ('14','15','16','30','31','1','2') else 0)

    return payday_column, df