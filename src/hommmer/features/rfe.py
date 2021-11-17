from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
import pandas as pd

def rfe(df, y_label, X_labels, max_features=None):
    if max_features is None:
        # A rule-of-thumb for a minimum number of data points for a stable linear regression 
        # are 7-10 data points per parameter.
        # https://storage.googleapis.com/pub-tools-public-publication-data/pdf/2d0395bc7d4d13ddedef54d744ba7748e8ba8dd1.pdf
        max_features = max(round(df.shape[0]/7),1)

    rfe = RFE(LinearRegression(), n_features_to_select=max_features).fit(df[X_labels], df[y_label])
    rfe_keep = pd.Series(rfe.support_)
    rfe_keep.index = X_labels
    
    rfe_df = pd.DataFrame({'rfe_keep': rfe_keep})
    rfe_df['rfe_ranking'] = rfe.ranking_
    return rfe_keep, rfe_df