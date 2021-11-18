import seaborn as sns

def lineplot(df, x_label, y_label):
    sns.lineplot(data=df, x=x_label,y=y_label)