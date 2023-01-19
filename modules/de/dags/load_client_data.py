import os
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from get_files import s3_to_table


with DAG(
    dag_id="load_client_data", catchup=False, start_date=datetime(2022, 1, 1)
) as dag:

    start = PythonOperator(
        task_id="start", python_callable=lambda: print("Data load started.")
    )
    end = PythonOperator(
        task_id="end", python_callable=lambda: print("Data load finished.")
    )

    # Loading base tables
    for fname in [
        "customer_activity.csv",
        "customer_profiles.csv",
        "labels.csv",
        "stores.csv",
    ]:
        load_file = PythonOperator(
            task_id=f"load_{fname}",
            python_callable=s3_to_table,
            op_kwargs={"fname": fname},
        )

        start >> load_file >> end
