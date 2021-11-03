import statsmodels.stats.api as sms
from statsmodels.compat import lzip

def jarque_bera(residuals):
    # Tests for normality of the residuals
    # skewness should be between -2 and 2
    # kurtosis should be between -7 and 7
    name = ['Jarque-Bera', 'Chi^2 prob', 'Skewness', 'Kurtosis']
    test = sms.jarque_bera(residuals)

    return lzip(name, test)