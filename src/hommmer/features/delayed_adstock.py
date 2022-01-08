import numpy as np

def delayed_adstock(x, L, P, D):
    '''
    params:
    x: original media variable, array
    L: length
    P: peak, delay in effect
    D: decay, retain rate
    returns:
    array, adstocked media variable
    '''
    # https://github.com/sibylhe/mmm_stan#12-adstock
    # prepend x with zeros equal to the length -1
    x = np.append(np.zeros(L-1), x)
    
    # create an array of zeros equal to the length
    weights = np.zeros(L)
    
    # loop through each day in length
    for l in range(L):
        # weight is decay to the power of index - peak squared
        weight = D**((l-P)**2)
        # add weight to weights in the right place (from back to front)
        weights[L-1-l] = weight
    
    # create an empty list
    adstocked_x = []
    # loop through length - 1 up to len(x)
    for i in range(L-1, len(x)):
        # get array of x from index - length + 1 to index + 1
        x_array = x[i-L+1:i+1]
        # sum the x_array * weights / sum(weights) to get adstock value
        xi = sum(x_array * weights)/sum(weights)
        # append adstocked value to adstocked_x
        adstocked_x.append(xi)
    
    # convert adstocked_x into an np.array
    adstocked_x = np.array(adstocked_x)
    
    # return adstocked_x
    return adstocked_x