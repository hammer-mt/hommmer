import pandas as pd

def make_geodate_index(df, date_label, geo_label):
    key_label = f"{date_label}${geo_label}"
    df[key_label] = pd.to_datetime(df[date_label]).astype(str) + "$" + df[geo_label]
    df.index = df[key_label]
    df.drop(key_label, axis=1, inplace=True)
    df.index.name = None