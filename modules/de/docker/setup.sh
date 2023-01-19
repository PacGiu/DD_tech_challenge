pip install -r /tmp/requirements.txt

export AIRFLOW_HOME=/opt/airflow
airflow db init
airflow users create -e "admin@airflow.com" -f "airflow" -l "airflow" -p "airflow" -r "Admin" -u "airflow"

airflow connections import /tmp/airflow_connections.json