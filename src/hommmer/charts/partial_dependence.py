from sklearn.inspection import plot_partial_dependence
# https://scikit-learn.org/stable/modules/partial_dependence.html

def partial_dependence(model, X_test, features):
    plot_partial_dependence(model, X_test, features)