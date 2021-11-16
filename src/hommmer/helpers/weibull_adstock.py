import numpy as np

# https://github.com/annalectnl/weibull-adstock/blob/master/adstock_weibull_annalect.pdf
# https://towardsdatascience.com/python-stan-implementation-of-multiplicative-marketing-mix-model-with-deep-dive-into-adstock-a7320865b334
def apply_weibull(x, window, k):
    '''
    params:
    x: original media variable, array
    window: length
    k: shape
    returns:
    array, adstocked media variable
    '''
    # prepend x with zeros equal to the window - 1
    x = np.append(np.zeros(window-1), x)
    
    # create an array of zeros equal to the window
    weights = np.zeros(window)
    
    # lambda is window / (-ln(0.001)) to the power of 1/k
    lam = window / (-np.log(0.001))**(1/k)
    
    # loop through each day in window
    for l in range(window):
        # weight is minus lag/lambda to the power of k exponentiated
        weight = np.exp(-(l/lam)**k)
        # add weight to weights in the right place (from front to back)
        weights[window-1-l] = weight
    
    # create an empty list
    adstocked_x = []
    # loop through window - 1 up to len(x)
    for i in range(window-1, len(x)):
        # get array of x from index - length + 1 to index + 1
        x_array = x[i-window+1:i+1]
        # sum the x_array * weights / sum(weights) to get adstock value
        xi = sum(x_array * weights)/sum(weights)
        # append adstocked value to adstocked_x
        adstocked_x.append(xi)
    
    # convert adstocked_x into an np.array
    adstocked_x = np.array(adstocked_x)
    
    # return adstocked_x
    return adstocked_x