def add_payday_dummies(df, date_label):
    df['payday'] = df[date_label].apply(lambda x:1 if x.strftime('%d') in ('14','15','16','30','31','1','2') else 0)

    return df