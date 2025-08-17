from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def start_number(**context):
    context['ti'].xcom_push(key='current_value', value=10)
    print("Starting number set to 10")

def add_five(**context):
    current_value = context['ti'].xcom_pull(key='current_value', task_ids='start_task')
    new_value= current_value + 5
    context['ti'].xcom_push(key='current_value' , value=new_value)
    print(f"Added 5, new value is {new_value}")

def multiply_by_two(**context):
    current_value = context['ti'].xcom_pull(key='current_value', task_ids='add_five_task')
    new_value = current_value * 2
    context['ti'].xcom_push(key='current_value', value=new_value)
    print(f"Multiplied by 2, new value is {new_value}")

def subtract_three(**context):
    current_value = context['ti'].xcom_pull(key='current_value', task_ids='multiply_task')
    new_value = current_value - 3
    context['ti'].xcom_push(key='current_value', value=new_value)
    print(f"Subtracted 3, new value is {new_value}")



with DAG(
    dag_id='math_operations_dag',
    start_date=datetime(2023, 10, 1),
    schedule='@once',
    catchup=False,
) as dag:

    start_task = PythonOperator(
        task_id='start_task',
        python_callable=start_number,
        provide_context=True
    )

    add_five_task = PythonOperator(
        task_id='add_five_task',
        python_callable=add_five,
        provide_context=True
    )

    multiply_task = PythonOperator(
        task_id='multiply_task',
        python_callable=multiply_by_two,
        provide_context=True
    )

    subtract_task = PythonOperator(
        task_id='subtract_task',
        python_callable=subtract_three,
        provide_context=True
    )

    start_task >> add_five_task >> multiply_task >> subtract_task