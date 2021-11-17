import pandas as pd

from .helpers import log, init_logging

def build(path, target, media, type="conversions", date="date", format="YYYY-MM-DD", verbose=False):
    init_logging(verbose)

    log("building a model")
    log(f"file: {path}")
    log(f"y={target}")
    log(f"X={media}")

    df = pd.read_csv(path)
    print(df)

