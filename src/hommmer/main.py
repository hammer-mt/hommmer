import pandas as pd

from .helpers import log, init_logging
from .cleaners import make_date_index
from .models import Linear, LogLinear, LogLog

def build(path, target, media, organic=None, date="date", verbose=False, override={}):
    init_logging(verbose)

    # load the dataframe and get the X_labels
    df = pd.read_csv(path)
    df.fillna(0, inplace=True)
    X_labels = list(df.columns)

    # remove target and date labels
    X_labels.remove(target)
    X_labels.remove(date)

    # if organic is not set, set it by removing media vars
    if organic is None:
        organic = X_labels.copy()
        for x in media:
            organic.remove(x)
    # if organic is set, remove anything not in media or organic
    else:
        for x in X_labels:
            if x not in media and x not in organic:
                X_labels.remove(x)

    # default settings
    settings = {
        "model": 'linear',
    }
    
    # override settings
    settings.update(override)

    # log model info
    log("building a model")
    log(f"file: {path}")
    log(f"y = {target}")
    log(f"X = {', '.join(X_labels)}")
    log(f"vars: {df.shape[1]}")
    log(f"obs: {df.shape[0]}")
    log(f"settings: {settings}")

    # make date the index
    make_date_index(df, date)

    # assign the y and X frames
    y = df[target]
    X = df[X_labels]

    # run model
    if settings['model'] == 'linear':
        return Linear(y, X, media)
    elif settings['model'] == 'log-linear':
        return LogLinear(y, X, media)
    elif settings['model'] == 'log-log':
        return LogLog(y, X, media)
    else:
        return Linear(y, X, media)


    

    

