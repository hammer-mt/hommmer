def del_X_labels(X_labels, del_cols):
    for x in del_cols:
        if x in X_labels:
            X_labels.remove(x)

    return X_labels