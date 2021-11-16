# https://facebookexperimental.github.io/Robyn/docs/variable-transformations/
def s_curve_saturation(x, alpha, gamma):
    """
    x = array
    alpha = shape
    gamma = inflection
    """
    return x**alpha / (x ** alpha + gamma ** alpha)