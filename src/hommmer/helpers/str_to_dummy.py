d = {
    "y": 1, "yes": 1, "t": 1, "true": 1, "on": 1, "1": 1, 
    "n": 0, "no": 0, "f": 0, "false": 0, "off": 0, "0": 0
    }

def str_to_dummy(series):
    return series.lower().map(d).astype(int)