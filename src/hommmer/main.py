from helpers import log, init_logging
from datasets import load_dataset

def build(path, target, media, type="conversions", date="date", format="YYYY-MM-DD", verbose=False):
    init_logging(verbose)

    log("building a model")
    log(f"file: {path}")
    log(f"y={target}")
    log(f"X={media}")

    df = load_dataset(path)

