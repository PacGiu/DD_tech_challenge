import time
import os
import psycopg2
import pandas as pd


def wait_for_table(table_name):
    """
    Call database untill the requestest table is found.
    Returns:
        df of table from database
    """
    # let the db start up
    print("Waiting for feature_store table...")
    time.sleep(5)

    # try to read feature_store
    table_is_not_up = True
    while table_is_not_up:
        try:
            # NOTE: connection must be within try, to avoid aborter transaction from psycopg2
            # TODO: read credentials from airflow_config
            connection = psycopg2.connect(
                database="companydata",
                user="admin",
                password=os.environ["ADMIN_DB_PASSWORD"],
                host="operational-db",
                port=5432,
            )
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            print(f"The table {table_name} is ready!")
            table_is_not_up = False
        except Exception as ex:
            print(f"Exception:{ex}")
            print(f"Waiting for {table_name} table...")
            time.sleep(30)

    # read dataframe
    df = pd.DataFrame(
        cursor.fetchall(), columns=[col.name for col in cursor.description]
    )
    return df
