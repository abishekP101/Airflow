from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(   
    dag_id='taskflow_api_dag',
    start_date=datetime(2023, 10, 1),
    schedule='@once',
    catchup=False
) as dag:
    
    @task
    def start_number():
        initial_value=10
        print(f"Initial value: {initial_value}")
        return initial_value
    
    @task
    def add_five(value):
        result = value + 5
        print(f"Value after adding five: {result}")
        return result
    
    @task
    def multiply_by_two(value):
        result = value * 2
        print(f"Value after multiplying by two: {result}")
        return result

    @task
    def subtract_three(value):
        result = value - 3
        print(f"Value after subtracting three: {result}")
        return result
    
    @task
    def square_number(value):
        result = value ** 2
        print(f"Value after squaring: {result}")
        return result
    
    start_value = start_number()
    added_value = add_five(start_value)
    multiplied_value = multiply_by_two(added_value)
    subtracted_value = subtract_three(multiplied_value)
    squared_value = square_number(subtracted_value)