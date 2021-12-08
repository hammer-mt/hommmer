import os
import pandas as pd

def load_holidays(download=True):
    path = os.path.join(os.path.dirname(__file__), "holidays.csv")
    df = pd.read_csv(path)
    if download:
        df.to_csv('holidays.csv', index=None)
        print("saving holidays.csv")
    else:
        return df