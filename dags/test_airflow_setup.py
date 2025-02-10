from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def print_hello():
    print("Hello from Airflow!")

def add_numbers():
    result = 1 + 1
    print(f"1 + 1 = {result}")

# Default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'basic_sample_dag',
    default_args=default_args,
    description='A simple DAG to test Airflow setup',
    schedule_interval=timedelta(days=1),
    catchup=False,
    tags=["hourly", "test"],
)

hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=print_hello,
    dag=dag,
)

add_task = PythonOperator(
    task_id='add_task',
    python_callable=add_numbers,
    dag=dag,
)

bash_task = BashOperator(
    task_id='bash_task',
    bash_command='echo "This is a Bash task running in Airflow"',
    dag=dag,
)

hello_task >> add_task >> bash_task
