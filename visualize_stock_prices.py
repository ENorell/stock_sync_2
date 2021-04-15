
import pandas as pd
import psycopg2

def load_data(schema, table, ticker):
    # First we set parameters for access details
    PGHOST = "localhost"
    PGDATABASE = "stock_data" # the name of our table 
    PGUSER = "stock_scraper" # your stock_scraper username
    PGPASSWORD = "tiger"
    # Set up a connection to the postgres server.
    conn_string = "host="+ PGHOST +" port="+ "5432" +" dbname="+ \
    PGDATABASE +" user=" + PGUSER \
    +" password="+ PGPASSWORD
    conn=psycopg2.connect(conn_string)
    # Create a cursor object
    cursor = conn.cursor()
    sql_command = f"SELECT * FROM {str(schema)}.{str(table)} WHERE ticker_intl=\'{ticker}\';"
    print (sql_command)
    # Load the data
    data = pd.read_sql(sql_command, conn)
    # and don't leave the connection open
    conn.close()
    return (data)

df = load_data('public','ticker_prices','ABB.ST')

df.head()