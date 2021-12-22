import datetime as dt
import pandas as pd
import numpy as np
from IPython.display import display
from timeit import default_timer as timer # https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python
from sklearn.model_selection import train_test_split

from hommmer.charts import accuracy
from hommmer.helpers import check_metric

class Model():
    def __init__(self, y, X, media_labels, settings):
        # set timestamp
        self.timestamp = dt.datetime.today().strftime('%Y-%m-%d %H:%M')

        # train-test split
        if settings['split']:
            X_train, X_test, y_train, y_test = train_test_split(X, y, 
                test_size=settings['split'], random_state=0)
        else:
            X_train, X_test, y_train, y_test = X, X, y, y

        
        # assign X and y
        self.X_actual = X
        self.y_actual = y
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        self.media_labels = media_labels

        # placeholders
        self.coefficients = []

    def _fit(self, y, X):
        return None

    def results(self):
        results_df = pd.DataFrame(self.contribution().sum(), columns=['contribution'])
        results_df['share'] = results_df['contribution'] / results_df['contribution'].sum() * 100
        results_df['coefficient'] = self.coefficients
        results_df['pvalue'] = self._pvalues()
        results_df = pd.concat([results_df, self._confidence_intervals()], axis=1)

        return np.around(results_df, 3)

    def contribution(self, X=None):
        if (X) is None:
            X = self.X_actual

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

    def metric(self, metric_label):
        value = check_metric(metric_label, self)
        return value[0]

    def show(self, charts=True, metrics=True, results=True):
        accuracy(self.y_actual, self.predict()) if charts else False
        self.metrics(["rsquared", "nrmse", "mape", "decomp-rssd", "cond-no"]) if metrics else False
        display(self.results()) if results else False