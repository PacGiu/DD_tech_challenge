import os
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
import psycopg2
import pandas as pd
import logging

with DAG(
    dag_id="monthly_avg_sales",
    catchup=False,
    start_date=datetime(2023, 1, 1),
    schedule_interval="@monthly",
) as dag:

    def print_table_fun():
        """
        Query monthly_avg_count and print it into airflow log
        """
        # TODO: read these credentials from airflow_config
        connection = psycopg2.connect(
            database="companydata",
            user="admin",
            password="admin",
            host="operational-db",
            port=5432,
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * from monthly_avg_count")

        df = pd.DataFrame(
            cursor.fetchall(), columns=[col.name for col in cursor.description]
        )

        logging.info("DATAFRAME OUTPUT:")
        logging.info(df.to_string())

    start = PythonOperator(
        task_id="start", python_callable=lambda: print("Data load started.")
    )

    end = PythonOperator(
        task_id="end", python_callable=lambda: print("Data load finished.")
    )

    create_monthly_avg_sales_table_if_not_exists = PostgresOperator(
        task_id="create_monthly_avg_sales_table_if_not_exists",
        postgres_conn_id="operational_db",
        sql="sql/create_monthly_avg_sales_table.sql",
    )

    aggregate_month_avg_sales = PostgresOperator(
        task_id="aggregate_month_avg_sales",
        postgres_conn_id="operational_db",
        sql="sql/aggregate_month_avg_sales.sql",
    )

    print_table = PythonOperator(
        task_id="print_table",
        python_callable=print_table_fun,
    )

    (
        start
        >> create_monthly_avg_sales_table_if_not_exists
        >> aggregate_month_avg_sales
        >> print_table
        >> end
    )
