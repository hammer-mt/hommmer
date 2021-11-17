import statsmodels.stats.api as sms
from statsmodels.compat import lzip

# need a way to run without passing results object
def harvey_collier(residuals, results, exog):
    # p-value should be less than 0.05
    name = ['t value', 'p value']
    test = sms.linear_harvey_collier(results)

    return lzip(name, test)