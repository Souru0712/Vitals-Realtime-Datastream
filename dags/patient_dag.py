import os  #for file & directory manipulation
import sys  #for Python runtime environment interaction
from datetime import datetime  #date module to return current date

from airflow import DAG  #allows the creation of DAG instances
from airflow.operators.python import PythonOperator  #allows DAG instances to call Python functions

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipelines.simulation_pipeline import simulation_pipeline
from pipelines.AWS_pipeline import AWS_pipeline

default_args = {
    'owner': 'Oscar',
    'start_date': datetime(2024, 11, 9)
}

#creating DAG instance
dag = DAG(
    dag_id='health_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=True,
    tags=['health', 'pipeline']
)

# creation of patients
generator = PythonOperator(
    task_id='patient_pipeline',
    python_callable=simulation_pipeline,
    provide_context=True,
    dag=dag
)  # upload to s3
upload_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable=AWS_pipeline,
    provide_context=True,
    dag=dag
)

generator >> upload_s3
