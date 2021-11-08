import matplotlib.pyplot as plt

def y_corr(df, y_label):
    plt.figure(figsize=(15,6))
    bars = df.corr()[y_label].sort_values(ascending=False).plot(kind='bar')
    plt.show()