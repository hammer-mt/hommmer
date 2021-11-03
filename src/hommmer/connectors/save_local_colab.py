from google.colab import files

def save_local_colab(df, file_name='abt'):

    file_name = file_name + '.csv'
    df.to_csv(file_name, index=False)
    files.download(file_name)