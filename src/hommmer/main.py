import pandas as pd

from .helpers import log, init_logging
from .cleaners import make_date_index
from .models import Linear, LogLinear, LogLog, Ridge, DeepLearning

def build(path, target, media, organic=None, date=None, override={}):
    # default settings
    settings = {
        "model": 'all',
        "split": 0.15,
        "metric": 'nrmse',
        "verbose": False
    }
    
    # override settings
    settings.update(override)
    
    init_logging(settings['verbose'])

    # load the dataframe and get the X_labels
    df = pd.read_csv(path)
    df.fillna(0, inplace=True)
    X_labels = list(df.columns)

    # guess date if not set
    if date is None:
        if 'date' in df.columns:
            date = 'date'
        elif 'Date' in df.columns:
            date = 'Date'
        else:
            date = df.columns[0]

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
        return Linear(y, X, media, settings)
    elif settings['model'] == 'log-linear':
        return LogLinear(y, X, media, settings)
    elif settings['model'] == 'log-log':
        return LogLog(y, X, media, settings)
    elif settings['model'] == 'ridge':
        return Ridge(y, X, media, settings)
    elif settings['model'] == 'deep-learning':
        return DeepLearning(y, X, media, settings)
    else:
        all_models = {
            'linear': Linear(y, X, media, settings),
            'log-linear': LogLinear(y, X, media, settings),
            'log-log': LogLog(y, X, media, settings),
            # 'ridge': Ridge(y, X, media, settings),
            # 'deep-learning': DeepLearning(y, X, media, settings)
            }
        accuracies = [{"model": x, f"{settings['metric']}": all_models[x].metric(settings['metric'])} for x in all_models.keys()]
        # min_error = min(all_models.keys(), key=lambda x: all_models[x].metric(settings['metric']))
        log("model accuracies:")
        log(accuracies)
        min_error = min(accuracies, key=lambda x: x[settings['metric']])
        return all_models[min_error['model']]


    

    

