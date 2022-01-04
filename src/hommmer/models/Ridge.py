import numpy as np
import statsmodels.api as sm
from timeit import default_timer as timer # https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python
from sklearn.linear_model import Ridge as SKRidge # https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html

from .Model import Model

class Ridge(Model):
    def __init__(self, y, X, media_labels, settings):
        # inheritance and start timer
        super().__init__(y, X, media_labels, settings, "Ridge")
        start = timer()

        # fit the model
        self._model = self._fit()

        # init required properties
        self.coefficients = self._coefficients()

        # finish running
        end = timer()
        self.runtime = end - start # Time in seconds, e.g. 5.38091952400282

        # log model locally
        self._save()

    ### EDIT BELOW HERE ###

    # fit the model
    def _fit(self):
        return SKRidge(alpha=0.01, fit_intercept=False).fit(self.X_train, self.y_train)

    # get the coefficients
    def _coefficients(self):
        return self._model.coef_
