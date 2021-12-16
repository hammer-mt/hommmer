from sklearn.inspection import plot_partial_dependence
def partial_dependence(model, X_test, features):
    plot_partial_dependence(model, X_test, features)