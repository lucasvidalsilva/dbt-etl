from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data_engineering_team',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'ipea_macro_elt',
    default_args=default_args,
    description='Pipeline ELT completo de dados macroeconômicos do IPEA',
    schedule='0 8 10 * *', # Todo dia 10 às 08:00, quando sai o IPCA
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=['finance', 'dbt', 'duckdb'],
) as dag:

   # INGESTÃO
    task_ingest = BashOperator(
        task_id='ingest_ipea_data',
        bash_command='python /opt/airflow/src/ingestion/ingest_ipea.py',
    )

    # TRANSFORMAÇÃO
    task_dbt_run = BashOperator(
        task_id='dbt_run_models',
        bash_command='cd /opt/airflow/dbt_project && dbt run --profiles-dir .',
    )

    # DBT TEST
    task_dbt_test = BashOperator(
        task_id='dbt_test_models',
        bash_command='cd /opt/airflow/dbt_project && dbt test --profiles-dir .',
    )

    # ordem de execução das tarefas
    task_ingest >> task_dbt_run >> task_dbt_test