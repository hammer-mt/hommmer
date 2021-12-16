import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import QuantileTransformer, OneHotEncoder, Normalizer
from sklearn import set_config
set_config(display='diagram')
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split,cross_validate
from joblib import load, dump
from sklearn.inspection import permutation_importance, plot_partial_dependence
from sklearn.metrics import mean_absolute_error as mae
from sklearn.utils import shuffle
from timeit import default_timer as timer # https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python

from .Model import Model

class DeepLearning(Model):
    def __init__(self, y, X, media_labels, settings):
        # inheritance and start timer
        super().__init__(y, X, media_labels, settings)
        start = timer()

        # fit the model
        self._model = self._fit()

        # finish running
        end = timer()
        self.runtime = end - start # Time in seconds, e.g. 5.38091952400282

    ### EDIT BELOW HERE ###

    # fit the model
    def _fit(self):
        all_features = list(self.X_train.columns)
        transformers = [
            ('scaler', QuantileTransformer(), all_features),
            ('normalizer',Normalizer(), all_features)
        ]
        ct = ColumnTransformer(transformers)
        steps =[
            ('column_transformer',ct),
            ('model', MLPRegressor(solver='lbfgs'))
            # solver 'lbfgs' is used for dataset with less than 1000 rows, if more than 1000 use solver 'adam'
            ]
        pipeline= Pipeline(steps)
        param_space={
            'column_transformer__scaler__n_quantiles':[80,100,120],
            'column_transformer__normalizer':[ Normalizer(), 'passthrough' ],
            'model__hidden_layer_sizes':[(35,35),(50,50),(75,75)],
            'model__alpha':[0.005, 0.001]
        }

        #input the param space into "param_grid", define what pipeline it needs to run, in our case is named "pipeline", and the you can decide how many cross validation can do "cv=" and the verbosity.
        grid = GridSearchCV(pipeline, param_grid=param_space, cv=3, verbose=2)
        grid.fit(self.X_train, self.y_train)
        return grid.best_estimator_

    ### OVERRIDE ###
    def contribution(self, X=None):
        if (X) is None:
            X = self.X_actual

        res = permutation_importance(self._model, X, self.y_actual, n_repeats=10)

        # create dataframe to collect results
        imp = pd.DataFrame(res['importances'].T, columns=X.columns)