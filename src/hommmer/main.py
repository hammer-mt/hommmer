from helpers import log, init_logging
from helpers import load_dataset, DATASETS

def build(path, target, media, type="conversions", date="date", format="YYYY-MM-DD", verbose=False):
    init_logging(verbose)

    log("building a model")
    log(f"file: {path}")
    log(f"y={target}")
    log(f"X={media}")

    if path in DATASETS:
        df = load_dataset(path)
    else:
        df = load_dataset(path)

