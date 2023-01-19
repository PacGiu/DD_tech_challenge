import os


def get_conn_string():
    """
    Gets the connection string for the Postgres database.
    Useful for inserting the base data from Pandas dataframes.
    """
    conn_string = f"postgresql+psycopg2://{os.environ['ADMIN_DB_USER']}:{os.environ['ADMIN_DB_PASSWORD']}@operational-db/companydata"
    return conn_string
