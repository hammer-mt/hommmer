import numpy as np
import statsmodels.api as sm
from timeit import default_timer as timer # https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python
from sklearn.linear_model import Ridge as SKRidge # https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html
from scipy import stats

from build.lib.hommmer.metrics.degrees_of_freedom import degrees_of_freedom

from .Model import Model

class Ridge(Model):
    def __init__(self, y, X, media_labels):
        # inheritance and start timer
        super().__init__(y, X, media_labels)
        start = timer()

        # fit the model
        self._model = self._fit()

        # init required properties
        self.coefficients = self._coefficients()
        self.significance = self._significance()
        self.uncertainty = self._uncertainty()

        # finish running
        end = timer()
        self.runtime = end - start # Time in seconds, e.g. 5.38091952400282

    ### EDIT BELOW HERE ###

    # fit the model
    def _fit(self):
        return SKRidge(alpha=0.01, fit_intercept=False).fit(self.X_train, self.y_train)

    # get the coefficients
    def _coefficients(self):
        return self._model.coef_

    # get the pvalues
    def _significance(self):
        # https://stackoverflow.com/questions/27928275/find-p-value-significance-in-scikit-learn-linearregression
        predictions = self.predict()
        newX = np.append(np.ones((len(self.X_train),1)), self.X_train, axis=1)
        MSE = (sum((self.y_train-predictions)**2))/(len(newX)-len(newX[0]))
        var_b = MSE*(np.linalg.inv(np.dot(newX.T,newX)).diagonal())
        std_errs = np.sqrt(var_b)
        t_values = self.coefficients / std_errs
        p_values = [2*(1-stats.t.cdf(np.abs(i),(len(newX)-len(newX[0])))) for i in t_values]
        return p_values

    # calculate the confidence intervals
    def _uncertainty(self):
        # https://stackoverflow.com/questions/27928275/find-p-value-significance-in-scikit-learn-linearregression
        predictions = self.predict()
        newX = np.append(np.ones((len(self.X_train),1)), self.X_train, axis=1)
        MSE = (sum((self.y_train-predictions)**2))/(len(newX)-len(newX[0]))
        var_b = MSE*(np.linalg.inv(np.dot(newX.T,newX)).diagonal())
        std_errs = np.sqrt(var_b)
        t_values = self.coefficients / std_errs
        dof = degrees_of_freedom(self.X_train.shape[1], self.X_train.shape[0])
        t_stat = stats.t.ppf(1-0.025, dof) # https://stackoverflow.com/questions/19339305/python-function-to-get-the-t-statistic
        moes = t_values * t_stat

        lower = self.coefficients - moes,
        upper = self.coefficients + moes

        return (upper - lower) / np.mean(self.y_train) * 100
