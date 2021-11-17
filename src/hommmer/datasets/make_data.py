from sklearn.datasets import make_regression
import datetime as dt
import pandas as pd

# generate regression dataset
def make_data(target_name="y", num_variables=5, num_significant=4, num_observations=180, noise=30):
    # Make sure not more significant than variables
    if num_significant > num_variables:
        num_significant = num_variables

    # Generate the regression data
    features, target = make_regression(n_samples=num_observations,
                                            n_features=num_variables,
                                            n_informative=num_significant,
                                            n_targets=1,
                                            noise=noise)

    variable_names = ['x'+str(i) for i in range(len(num_variables))]
        
    # Create dataframe
    df = pd.DataFrame(features, columns=variable_names)

    # Add target data
    df[target_name] = target

    return df
