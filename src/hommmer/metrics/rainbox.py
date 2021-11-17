import statsmodels.stats.api as sms
from statsmodels.compat import lzip

# need a way to run without passing results object
def rainbox(residuals, results, X_labels):
    # tests for linearity
    # p-value should be less than 0.05
    name = ['rainbow F stat', 'rainbow F stat p-value']
    test = sms.linear_rainbow(results)
    return lzip(name, test)