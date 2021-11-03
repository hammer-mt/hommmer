import statsmodels.stats.api as sms

def breuschpagan(residuals, exog):
    # tests for heteroskedasticity
    # p-value should be less than 0.05
    name = ['Lagrange', 'p-value','f-value', 'f p-value']
    test = sms.het_breuschpagan(residuals, exog)