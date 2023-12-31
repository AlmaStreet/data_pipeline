# data_pipeline

## list all existing DAGS
```
airflow dags list
```

## list out all tasks in DAG named 'example_bash_operator'
```
airflow tasks list example_bash_operator
```

## pause/unpause DAG
```
airflow dags unpause tutorial
airflow dags pause tutorial
```