import numpy as np
import statsmodels.api as sm
import pandas as pd
from timeit import default_timer as timer # https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python

from .Model import Model
from hommmer.helpers import log_ex_zeros

# https://www.spencertom.com/2020/08/29/marketing-mix-modeling-mmm-part-3-of-3/
# https://stats.stackexchange.com/questions/140713/making-predictions-with-log-log-regression-model
# https://davegiles.blogspot.com/2014/12/s.html
class LogLinear(Model):
    def __init__(self, y, X, media_labels, settings):
        # inheritance and start timer
        super().__init__(y, X, media_labels, settings)
        start = timer()

        # fit the model
        self._model = self._fit()

        # init required properties
        self.coefficients = self._coefficients()

        # finish running
        end = timer()
        self.runtime = end - start # Time in seconds, e.g. 5.38091952400282

    ### EDIT BELOW HERE ###

    # fit the model
    def _fit(self):
        logged_y = np.log(self.y_train + 1)
        return sm.OLS(logged_y, self.X_train).fit()  # log y

    # get the coefficients
    def _coefficients(self):
        return self._model.params.values

    # get the pvalues
    def _pvalues(self):
        return self._model.pvalues

    # calculate the confidence intervals
    def _confidence_intervals(self):
        conf_int_df = self._model.conf_int()
        conf_int_df.columns = ["lower", "upper"]
        return (conf_int_df["upper"] - conf_int_df["lower"]) / np.mean(self.y_train) * 100

    ### OVERRIDE BASE FUNCS ###
    def contribution(self, X=None):
        if (X) is None:
            X = self.X_train

        coef_df = pd.DataFrame({'coefficient': self.coefficients}, index=X.columns)

        data = []
        for x in list(X.columns):
            contrib = coef_df['coefficient'].loc[x] * X[x]
            data.append(contrib)

        contrib_df = pd.DataFrame(data).T
        exp_contrib_df = contrib_df.copy()
        # transform log y back into y
        for x in contrib_df:
            contrib_share = contrib_df[x] / contrib_df.sum() 
            exp_contrib_df[x] = np.exp(contrib_df[x]) - contrib_share # exp y and remove 1

        return exp_contrib_df


    



