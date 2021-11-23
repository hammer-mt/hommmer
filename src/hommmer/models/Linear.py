import numpy as np
import pandas as pd
import statsmodels.api as sm
from timeit import default_timer as timer # https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python
import datetime as dt
from IPython.display import display

from hommmer.charts import accuracy
from hommmer.helpers import check_metric

class Linear():
    def __init__(self, X, y, media_labels):
        # start running
        start = timer()
        self.timestamp = dt.datetime.today().strftime('%Y-%m-%d %H:%M')
        
        # assign X and y
        self.X_train = X
        self.y_train = y
        self.media_labels = media_labels

        # fit the model
        self._model = sm.OLS(y, X).fit()

        # get coefficients and pvalues
        self.coefficients = self._model.params.values
        self.pvalues = self._model.pvalues.values

        # confidence intervals
        conf_int = self._model.conf_int()
        conf_int.columns = ["lower", "upper"]
        conf_int['% MoE'] = (conf_int["upper"] - conf_int["lower"]) / np.mean(y)
        self.confidence_intervals = conf_int

        # finish running
        end = timer()
        self.runtime = end - start # Time in seconds, e.g. 5.38091952400282

    def predict(self, X=None):
        if (X) is None:
            X = self.X_train
        y_pred = self._model.predict(X)
        return y_pred

    def contribution(self, X=None):
        if (X) is None:
            X = self.X_train

        coef_df = pd.DataFrame({'coefficient': self.coefficients}, index=X.columns)

        data = []
        for x in list(X.columns):
            contrib = coef_df['coefficient'].loc[x] * X[x]
            data.append(contrib)

        contrib_df = pd.DataFrame(data).T
        return contrib_df

    def metrics(self, metric_labels):
        metrics = []
        for metric in metric_labels:
            
            value = check_metric(metric, self)
            metrics.append((metric, value))
        for label, output in metrics:
            print(f"{output[1]} {label}: {output[0]}")

    def results(self):
        results_df = pd.DataFrame(self.contribution().sum(), columns=['contribution'])
        results_df['coefficients'] = self.coefficients
        results_df['pvalues'] = self.pvalues
        results_df = pd.concat([results_df, self.confidence_intervals], axis=1)

        return np.around(results_df, 3)

    def show(self, charts=True, metrics=True, results=True):
        accuracy(self.y_train, self.predict()) if charts else False
        self.metrics(["nrmse", "rsquared", "decomp_rssd"]) if metrics else False
        display(self.results()) if results else False


    



