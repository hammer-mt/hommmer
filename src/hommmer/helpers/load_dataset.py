import pandas as pd
from helpers.logging import log

DATASETS = ["duff.csv"]

def load_dataset(file_name):
    log("loading dataset {file_name}")
    df = pd.read_csv(file_name)
    return df
