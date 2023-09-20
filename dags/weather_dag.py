from datetime import datetime
from airflow import DAG

from airflow.operators.python import PythonVirtualenvOperator, PythonOperator

from chart import create_chart
from data import download_data

dag = DAG(
    dag_id="weather_data",
    start_date=datetime(2023, 8, 12),
    schedule="@daily",

)

extract_data = PythonOperator(
    task_id="extract_data",
    python_callable=download_data,
    dag=dag,
    op_kwargs={"places": ["London", "Berlin"], "api_key": "69d04041455dad24ba5e9a7a0ef3903e"}
)

create_chart = PythonVirtualenvOperator(
    task_id="create_chart",
    requirements=["pandas", "matplotlib"],
    python_callable=create_chart,
    dag=dag,
)

extract_data >> create_chart







