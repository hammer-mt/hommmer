def get_all_X_labels(columns, y_label, date_label):
    X_labels = columns.copy()
    X_labels.remove(y_label)
    X_labels.remove(date_label)
    
    return X_labels