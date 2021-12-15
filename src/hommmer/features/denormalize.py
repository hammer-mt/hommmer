# https://stackoverflow.com/questions/51471672/reverse-z-score-pandas-dataframe
def denormalize(x_trans, x, method="mean"):
    if method == "minmax":
        return (x.max()-x.min())*x_trans+x.min()
    else:
        return x_trans*x.std()+x.mean()