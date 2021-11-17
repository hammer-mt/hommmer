from statsmodels.stats.outliers_influence import variance_inflation_factor
import numpy as np
import pandas as pd
np.seterr(divide='ignore', invalid='ignore') # hide error warning for vif

def vif(df, X_labels, max_vif=5):
    # Variance Inflation Factor (VIF)
    # tests for colinearity: A VIF of over 10 for some feature indicates that over 90% 
    # of the variance in that feature is explained by the remaining features. Over 100 
    # indicates over 99%. Best practice is to keep variables with a VIF less than 5.

    X = df[X_labels]
    X_np = np.array(X)

    vif_results = [(X.columns[i], variance_inflation_factor(X_np, i)) for i in range(X_np.shape[1])]
    vif_df = pd.DataFrame(vif_results)
    vif_df.columns = ['idx', 'vif']
    vif_df.index = vif_df['idx']
    vif_df.drop(['idx'], axis=1, inplace=True)
    vif_df.index.name = None
    vif_df['vif_keep'] = vif_df['vif'] < max_vif
    
    vif_keep = list(vif_df[vif_df['vif_keep']==True].index.values)

    return vif_keep, vif_df