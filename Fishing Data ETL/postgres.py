# CONNECT TO POSTGRESQL DATABASE
def connect_postgres(host, database, user, password):
    import psycopg2
    from sqlalchemy import create_engine
    from urllib.parse import quote_plus

    db_params = {
        "host": host,
        "database": database,
        "user": user,
        "password": password,
    }

    global conn
    global cursor
    global connect
    global engine


    conn = psycopg2.connect(**db_params)
    # Create a cursor
    cursor = conn.cursor()
    

    # Encode the password
    encoded_password = quote_plus(db_params["password"])
    db_params["password"] = encoded_password

    engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}/{db_params["database"]}')
    connect = engine.connect()



# USE CONNECT_POSTGRES FUNCTION FIRST!!!
# DATAFRAME MUST BE IN PANDAS DATAFRAME AND RENAME YOUR DATAFRAME AS "df" OBJECT
# IF NOT THEN JUST CONNECT OWN DATAFRAME OBJECT
def postgres_upload(schema, table, dataframe, mode = 'replace'): 
    import pandas as pd
    from sqlalchemy import inspect

    try: 
        # REPLACES THE TABLE IF EXISTS ... use 'append' if append
        dataframe.to_sql(table, engine, schema = schema, if_exists=mode, index=False)
    
    except Exception as e:
        print(f'Error uploading: {e}')


