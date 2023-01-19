#!/bin/bash
airflow scheduler &
airflow webserver --port 8082
