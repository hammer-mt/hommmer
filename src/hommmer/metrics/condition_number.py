import numpy as np
def condition_number(X):
    # tests for multicollinearity
    # condition number should be less than 30
    value = round(np.linalg.cond(X))
    passed = "✔️" if value < 30 else "❌"
    return value, passed