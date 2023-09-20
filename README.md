# weatherETL
An ETL pipe line to work with weather data using Apache Airflow.
The weather_dag.py employs PythonVirtualenvOperator to install required dependencies before executing the "chart" task.

## How to run
Create a new folder and clone the repo.

The folder includes a docker-compose.yaml file you can use to build an Apache Airflow local instance:

```docker compose up```


