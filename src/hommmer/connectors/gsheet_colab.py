from google.colab import auth
import gspread
from oauth2client.client import GoogleCredentials
import pandas as pd

### NOTE: this only works in Google Colab

def gsheet_colab(url, offset=None):
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