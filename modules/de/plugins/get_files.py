from get_conn_string import get_conn_string
import os


def get_file_from_s3(fname):
    """
    Read an s3 file into a Pandas dataframe.
    """
    import pandas as pd
    import boto3

    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        region_name="eu-west-1",
    )
    data = s3.get_object(Bucket="daredata-technical-challenge-data", Key=fname)
    data = pd.read_csv(data["Body"])

    return data


def s3_to_table(fname):
    """
    Reads an s3 file and creates a new table in the database with the contents of this file.
    """
    data = get_file_from_s3(fname)
    data.to_sql(
        fname.split(".csv")[0], get_conn_string(), index=False, if_exists="replace"
    )


def get_prev_month_sales(**context):
    """Gets the sales for the current month, based on an Airflow DAG run."""
    month = context["data_interval_start"].strftime("%Y-%m-%d")
    fname = f"sales/{month}/sales.csv"

    data = get_file_from_s3(fname=fname)

    data.to_sql("sales", get_conn_string(), index=False, if_exists="append")
