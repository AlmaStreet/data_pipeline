# import the libraries
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

# defining DAG arguments
default_args = {
    "owner": "Jason",
    "start_date": datetime.today(),
    "email": "dummy_email@gmail.com",
    "email_on_failure": True,
    "email_on_retry": True,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# define the DAG
dag = DAG(
    "ETL_toll_data",
    default_args=default_args,
    description="Apache Airflow Final Assignment",
    schedule_interval=timedelta(days=1),
)

# Download the file here
# wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz

# define the first task (task 1.3)
unzip_data = BashOperator(
    task_id="unzip_data",
    bash_command="tar -xzf tolldata.tgz",
    dag=dag,
)

# define the second task (task 1.4)
extract_data_from_csv = BashOperator(
    task_id="extract_data_from_csv",
    bash_command='cut -d"," -f1,2,3,4 vehicle-data.csv > csv_data.csv',
    dag=dag,
)

# define the third task (task 1.5)
extract_data_from_tsv = BashOperator(
    task_id="extract_data_from_tsv",
    bash_command="cut -d$'\t' -f5,6,7 tollplaza-data.tsv > tsv_data.csv",
    dag=dag,
)

# define the fourth task (task 1.6)
extract_data_from_fixed_width = BashOperator(
    task_id="extract_data_from_fixed_width",
    bash_command="cut -c59- payment-data.txt > fixed_width_data.csv",
    dag=dag,
)

# define the fifth task (task 1.7)
consolidate_data = BashOperator(
    task_id="consolidate_data",
    bash_command="paste csv_data.csv tsv_data.csv fixed_width_data.csv > extracted_data.csv",
    dag=dag,
)

# define the sixth task (task 1.8)
transform_data = BashOperator(
    task_id="transform_data",
    bash_command="tr '[:lower:]' '[:upper:]' < extracted_data.csv > transformed_data.csv",
    dag=dag,
)

(
    unzip_data
    >> extract_data_from_csv
    >> extract_data_from_tsv
    >> extract_data_from_fixed_width
    >> consolidate_data
    >> transform_data
)
