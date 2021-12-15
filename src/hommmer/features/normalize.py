# standardize variable
def normalize(x, method="mean"):
    if method == "minmax":
        return (x-x.min())/(x.max()-x.min())
    else:
        return (x - x.mean())/x.std()
