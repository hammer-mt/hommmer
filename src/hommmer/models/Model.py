import datetime as dt
from IPython.display import display

from hommmer.charts import accuracy
from hommmer.helpers import check_metric

class Model():
    def __init__(self, X, y, media_labels):
        # start running
        self.timestamp = dt.datetime.today().strftime('%Y-%m-%d %H:%M')
        
        # assign X and y
        self.X_train = X
        self.y_train = y
        self.media_labels = media_labels

        # placeholders
        self._model = None
        self.coefficients = []
        self.pvalues = []
        self.confidence_intervals = None

    def predict(self, X=None):
        return None

    def contribution(self, X=None):
        return None

    def metrics(self, metric_labels):
        metrics = []
        for metric in metric_labels:
            
            value = check_metric(metric, self)
            metrics.append((metric, value))
        for label, output in metrics:
            print(f"{output[1]} {label}: {output[0]}")

    def results(self):
        return None

    def show(self, charts=True, metrics=True, results=True):
        accuracy(self.y_train, self.predict()) if charts else False
        self.metrics(["nrmse", "rsquared", "decomp_rssd"]) if metrics else False
        display(self.results()) if results else False