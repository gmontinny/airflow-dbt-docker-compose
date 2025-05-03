"""
A DAG that demonstrates how to run DBT commands in Airflow.
This DAG will run a simple DBT project that creates a view based on information_schema.tables.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

# Define the DAG
dag = DAG(
    'dbt_example',
    default_args=default_args,
    description='A DAG that runs DBT commands',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    catchup=False,
    tags=['dbt', 'example'],
)

# Set the DBT project directory
dbt_project_dir = '/opt/airflow/dbt_project'

# Task to run DBT debug (checks if DBT can connect to the database)
dbt_debug = BashOperator(
    task_id='dbt_debug',
    bash_command=f'cd {dbt_project_dir} && dbt debug --profiles-dir {dbt_project_dir}',
    dag=dag,
)

# Task to run DBT compile (compiles the SQL but doesn't run it)
dbt_compile = BashOperator(
    task_id='dbt_compile',
    bash_command=f'cd {dbt_project_dir} && dbt compile --profiles-dir {dbt_project_dir}',
    dag=dag,
)

# Task to run DBT run (runs the models)
dbt_run = BashOperator(
    task_id='dbt_run',
    bash_command=f'cd {dbt_project_dir} && dbt run --profiles-dir {dbt_project_dir}',
    dag=dag,
)

# Task to run DBT test (runs tests on the models)
dbt_test = BashOperator(
    task_id='dbt_test',
    bash_command=f'cd {dbt_project_dir} && dbt test --profiles-dir {dbt_project_dir}',
    dag=dag,
)

# Task to generate DBT documentation
dbt_docs_generate = BashOperator(
    task_id='dbt_docs_generate',
    bash_command=f'cd {dbt_project_dir} && dbt docs generate --profiles-dir {dbt_project_dir}',
    dag=dag,
)

# Set the task dependencies
dbt_debug >> dbt_compile >> dbt_run >> dbt_test >> dbt_docs_generate
