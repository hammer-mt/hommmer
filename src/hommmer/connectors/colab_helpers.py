### NOTE: these functions only work in Google Colab

def save_local(df, file_name='abt'):
    from google.colab import files
    file_name = file_name + '.csv'
    df.to_csv(file_name, index=False)
    files.download(file_name)


def upload_local():
    from google.colab import files
    uploaded = files.upload()
    return uploaded


def load_gsheet(url, offset=None):
    from google.colab import auth
    import gspread
    from oauth2client.client import GoogleCredentials
    import pandas as pd
    # authorize google sheets
    auth.authenticate_user()

    gc = gspread.authorize(GoogleCredentials.get_application_default())

    spreadsheet = gc.open_by_url(url)
    sheet =  spreadsheet.get_worksheet(0)

    if offset is None:
        df = pd.DataFrame(sheet.get_all_records())
    else:
        df = pd.DataFrame(sheet.get_all_values()[offset:])
        df.columns = df.iloc[0]
        df.drop([0], inplace=True)

    return df