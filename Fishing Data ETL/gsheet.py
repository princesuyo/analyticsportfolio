# Read gsheet into pandas dataframe object "df"
# Sheet is the sheet name 
# URL is the url of the spreadsheet
def get_gsheet_df(url, sheet):
    import googleapiclient
    from gsheets import Sheets
 
    creds = '''
                ### Gsheet API
            '''
    sheets = Sheets.from_files(creds)

    #global df
    global df
    global s 
    while True:
        timeout_count = 0
        httperror_count = 0
        
        try:
            #global df
            s = sheets.get(url)

            # GET WORKSHEET. CHANGE SHEET NAME IF NEEDED
            df = s.find(sheet).to_frame()
            print(f'{sheet} read to dataframe.')

            return df

        except TimeoutError as e:
                print(f'Timeout Error: {url}')
                #url_errors.append(url)
                if timeout_count < 2:
                    print('Retrying...')
                    timeout_count += 1
                    continue
                else:
                    #url_errors.append(url)
                    print('Max retries done. Retry again later...')
                    break
            
        except googleapiclient.errors.HttpError as e:
            #url_errors.append(url)
            print(f'Http Error: {url}')
            if httperror_count < 2:
                print('Retrying...')
                httperror_count += 1
                continue
            else:
                #url_errors.append(url)
                print('Max retries done. Retry again later...')
                break