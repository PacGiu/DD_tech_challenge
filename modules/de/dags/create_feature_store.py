import datetime

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator


with DAG(
    dag_id="process_data",
    start_date=datetime.datetime(2022, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    # Creating table with only the latest customer activity
    drop_table_customer_activity_latest = PostgresOperator(
        task_id="drop_table_customer_activity_latest",
        postgres_conn_id="operational_db",
        sql="sql/drop_table_customer_activity_latest.sql",
    )

    create_table_customer_activity_latest = PostgresOperator(
        task_id="create_table_customer_activity_latest",
        postgres_conn_id="operational_db",
        sql="sql/create_table_customer_activity_latest.sql",
    )

    # Joining all static features, customer activity, and labels
    # to create the feature store
    # (going for the lazy approach of dropping/recreating every time)
    drop_feature_store = PostgresOperator(
        task_id="drop_feature_store",
        postgres_conn_id="operational_db",
        sql="sql/drop_feature_store.sql",
    )

    create_feature_store = PostgresOperator(
        task_id="create_feature_store",
        postgres_conn_id="operational_db",
        sql="sql/create_feature_store.sql",
    )

    # Granting access permissions to the DS user
    grant_access = PostgresOperator(
        task_id="grant_access",
        postgres_conn_id="operational_db",
        sql="GRANT SELECT ON TABLE feature_store TO ds_user_role",
    )

    # Start and end tasks
    start = PythonOperator(
        task_id="start", python_callable=lambda: print("Data processing started.")
    )
    end = PythonOperator(
        task_id="end", python_callable=lambda: print("Data processing finished.")
    )

    # Ordering tasks
    (
        start
        >> [drop_table_customer_activity_latest, drop_feature_store]
        >> create_table_customer_activity_latest
        >> create_feature_store
        >> grant_access
        >> end
    )
