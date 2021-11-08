from sklearn.model_selection import train_test_split

def train_test_split(df, y_label, X_labels):
    X = df[X_labels]
    y = df[y_label]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    return X_train, X_test, y_train, y_test