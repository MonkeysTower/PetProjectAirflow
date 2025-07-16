from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Добавляем пути к src, чтобы можно было импортировать модули
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.extract.user_extractor import extract_user
from src.transform.user_transformer import transform_user
from src.load.user_loader import load_user


default_args = {
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}


def run_extract(**kwargs):
    user = extract_user()
    kwargs['ti'].xcom_push(key='raw_user', value=user)


def run_transform(**kwargs):
    ti = kwargs['ti']
    raw_user = ti.xcom_pull(key='raw_user', task_ids='extract_task')
    transformed = transform_user(raw_user)
    ti.xcom_push(key='transformed_user', value=transformed)


def run_load(**kwargs):
    ti = kwargs['ti']
    transformed_user = ti.xcom_pull(key='transformed_user', task_ids='transform_task')
    load_user(transformed_user)


with DAG(
    dag_id='etl_randomuser_pipeline',
    default_args=default_args,
    description='ETL-процесс с разделением на слои и JSON-логами',
    schedule=timedelta(minutes=1),
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id='extract_task',
        python_callable=run_extract,
    )

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=run_transform,
    )

    load_task = PythonOperator(
        task_id='load_task',
        python_callable=run_load,
    )

    extract_task >> transform_task >> load_task