from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

from datetime import datetime

args = {
    "owner": "Americo", 
    "start_date": days_ago(1), 
    "cpus":4, 
    "ram":2048, 
    "disk":2048
    }

dag = DAG(
    dag_id='pipeline_bash_operator',
    default_args=args,
    start_date=days_ago(1), 
    schedule_interval='@once',
)
with dag:
    t1 = BashOperator(
        task_id='run_script_ingest',
        bash_command='python /opt/airflow/dags/Proyecto/ingest.py',
    )
    t2 = BashOperator(
        task_id='run_script_transform',
        bash_command='python /opt/airflow/dags/Proyecto/transform.py',
    )
    t3 = BashOperator(
        task_id='run_script_load',
        bash_command='python /opt/airflow/dags/Proyecto/load.py',
    )

    t1 >> t2 >> t3