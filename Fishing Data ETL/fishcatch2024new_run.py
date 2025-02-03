from postgres import connect_postgres, postgres_upload
from gsheet import get_gsheet_df
import warnings

def job():
    print('Program Started...')
    warnings.filterwarnings('ignore')

    url = '' # URL
    sheet = '' # SHEET
    db_login = {
        'database':'', # DATABASE
        'user':'', # USERNAME
        'password':'' # PASSWORD
    }

    try:
        df = get_gsheet_df(url = url, sheet = sheet)
        #print(df.head())
        df.dropna(subset = '', inplace = True)

        connect_postgres(**db_login)
        #connect = connect_postgres(**db_login)
        postgres_upload(schema = '', table = '', dataframe = df)

        print(f'{len(df)} lines uploaded. \n')

    except Exception as e:
        print(f'Error: {e}')

    

if __name__ == '__main__':
    job()