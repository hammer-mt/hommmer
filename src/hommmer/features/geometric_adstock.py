import statsmodels.tsa.api as tsa

def geometric_adstock(x, theta):
    return tsa.filters.recursive_filter(x, theta)