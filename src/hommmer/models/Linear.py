import numpy as np
import statsmodels.api as sm
from timeit import default_timer as timer # https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python

from .Model import Model

class Linear(Model):
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
        return sm.OLS(self.y_train, self.X_train).fit()

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
        conf_int_df['uncertainty'] = (conf_int_df["upper"] - conf_int_df["lower"]) / np.mean(self.y_train) * 100
        return conf_int_df


    



