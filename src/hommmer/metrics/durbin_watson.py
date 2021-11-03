import statsmodels.stats.api as sms

def durbin_watson(residuals):
    # tests for autocorrelation
    # durbin watson should be between 1.5 and 2.5
    test = sms.durbin_watson(residuals)
    return ('Durbin Watson', test)