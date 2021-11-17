import os
import pandas as pd

def load_duff():
    path = os.path.join(os.path.dirname(__file__), "duff.csv")
    df = pd.read_csv(path)
    df.to_csv('duff.csv', index=None)
    print("saving duff.csv")