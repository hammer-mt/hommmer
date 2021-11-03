import numpy as np
def condition_number(exog):
    # tests for multicollinearity
    # condition no should be less than 30
    condition = np.linalg.cond(exog)