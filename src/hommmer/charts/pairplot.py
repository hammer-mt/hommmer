import matplotlib.pyplot as plt
import seaborn as sns

def pairplot(df, y_label):
    sns.pairplot(df)
    plt.show()