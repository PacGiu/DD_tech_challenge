# DE Module

## Docker Containers

### Airflow Web Server

UI for the Airflow instance that will be running your dags.

- URL: http://localhost:8080
- Default Login: airflow / airflow

### Operational DB
The database where the sales data are and where you will be creating the aggregated tables.

- Host: operational-db
- Port: 5432
- Default Login: admin / admin
- Database Name: companydata

## Folder Structure

* `dags`: contains the Airflow DAGs to process and load the data.
    * `sql`: contains the SQL files used by the DAGs
* `db_admin`: contains the configuration SQL files that run upon starting the database for the first time. Used to create the users, for example.
* `docker`: configures the Docker image, as well as the Airflow -> Database connection.
* `plugins`: custom Python code required for the DAGs.