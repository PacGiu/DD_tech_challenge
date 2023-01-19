import os
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

from get_files import get_prev_month_sales


with DAG(
    dag_id="load_sales_data",
    catchup=True,
    start_date=datetime(2023, 1, 1),
    schedule_interval="@monthly",
) as dag:

    start = PythonOperator(
        task_id="start", python_callable=lambda: print("Data load started.")
    )
    end = PythonOperator(
        task_id="end", python_callable=lambda: print("Data load finished.")
    )

    # Creating sales table if it doesn't exist and insert the latest month of data
    create_sales_table_if_not_exists = PostgresOperator(
        task_id="create_sales_table_if_not_exists",
        postgres_conn_id="operational_db",
        sql="sql/create_sales_table.sql",
    )

    get_prev_month_sales = PythonOperator(
        task_id=f"get_prev_month_sales", python_callable=get_prev_month_sales
    )

    # Creating table for monthly sales, and aggregating the latest month of data
    create_monthly_sales_table_if_not_exists = PostgresOperator(
        task_id="create_monthly_sales_table_if_not_exists",
        postgres_conn_id="operational_db",
        sql="sql/create_monthly_sales_table.sql",
    )

    aggregate_past_month_sales = PostgresOperator(
        task_id="aggregate_past_month_sales",
        postgres_conn_id="operational_db",
        sql="sql/aggregate_past_month_sales.sql",
    )

    (
        start
        >> create_sales_table_if_not_exists
        >> get_prev_month_sales
        >> create_monthly_sales_table_if_not_exists
        >> aggregate_past_month_sales
        >> end
    )
