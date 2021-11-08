import pandas as pd
import statsmodels.api as sm
import time

class Linear():
    def __init__(self, X, y):
        start_time = time.time()
        self.model = sm.OLS(y, X).fit()
        self.run_time = round((time.time() - start_time)/60,2)

    def run_time(self):
        return self.run_time

    def predict(self, X):
        y_pred = self.model.predict(X)

    def significance(self):
        p_values = self.model.pvalues.values
        return p_values

    def contribution(self, X):
        coefs = self.model.params.values
        X_labels = list(X.columns)
        coef_df = pd.DataFrame({'coef': coefs}, index=X_labels)

        data = []
        for x in X_labels:
            contrib = coef_df['coef'].loc[x] * X[x]
            data.append(contrib)

        contrib_df = pd.DataFrame(data, columns=X.columns)
        return contrib_df


    



