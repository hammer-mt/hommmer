import datetime as dt
import pandas as pd
import numpy as np
from IPython.display import display
from timeit import default_timer as timer # https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python

from hommmer.charts import accuracy
from hommmer.helpers import check_metric

class Model():
    def __init__(self, y, X, media_labels):
        # set timestamp
        self.timestamp = dt.datetime.today().strftime('%Y-%m-%d %H:%M')
        
        # assign X and y
        self.X_train = X
        self.y_train = y
        self.media_labels = media_labels

        # placeholders
        self.coefficients = []
        self.pvalues = []
        self.confidence_intervals = None

    def _fit(self, y, X):
        return None

    def results(self):
        results_df = pd.DataFrame(self.contribution().sum(), columns=['contribution'])
        results_df['coefficients'] = self.coefficients
        results_df['pvalues'] = self.pvalues
        results_df = pd.concat([results_df, self.confidence_intervals], axis=1)

        return np.around(results_df, 3)

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

    def predict(self, X=None):
        contribution = self.contribution(X)
        y_pred = contribution.sum(axis=1)
        return y_pred

    def metrics(self, metric_labels):
        metrics = []
        for metric in metric_labels:
            
            value = check_metric(metric, self)
            metrics.append((metric, value))
        for label, output in metrics:
            print(f"{output[1]} {label}: {output[0]}")

    def show(self, charts=True, metrics=True, results=True):
        accuracy(self.y_train, self.predict()) if charts else False
        self.metrics(["nrmse", "rsquared", "decomp_rssd"]) if metrics else False
        display(self.results()) if results else False