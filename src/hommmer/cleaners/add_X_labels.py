def add_X_labels(X_labels, add_cols):
    for x in add_cols:
        if x not in X_labels:
            X_labels.append(x)

    return X_labels