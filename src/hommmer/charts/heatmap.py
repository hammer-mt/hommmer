import matplotlib.pyplot as plt
import seaborn as sns

def heatmap(df):
    plt.figure(figsize=(15,6))
    heatmap = sns.heatmap(df.corr(), annot=True, cmap="Blues")
    plt.show()