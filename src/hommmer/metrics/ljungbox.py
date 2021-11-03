import statsmodels.stats.api as sms
from statsmodels.compat import lzip

def ljungbox(residuals, X_labels):
    # tests for autocorrelation
    # p-value should be less than 0.05
    name = ['Ljung-Box stat', 'p-value']
    lags = min(len(X_labels)/2-2, 40)
    test = sms.acorr_ljungbox(residuals, lags=[lags])
    return lzip(name, test)