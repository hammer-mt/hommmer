import os
import pandas as pd

def load_duff(download=True):
    path = os.path.join(os.path.dirname(__file__), "duff.csv")
    df = pd.read_csv(path)
    if download:
        df.to_csv('duff.csv', index=None)
        print("saving duff.csv")
    else:
        return df