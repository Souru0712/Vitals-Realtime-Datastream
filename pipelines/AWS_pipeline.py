from etls.AWS_store import connect_to_AWS, print_all_buckets, upload_to_bucket
from datetime import datetime

def AWS_pipeline(ti, execution_date:datetime): #task instance
    #connect
    s3 = connect_to_AWS()
    print_all_buckets(s3)

    #load
    file_path = ti.xcom_pull(task_ids='patient_pipeline', key='return_value')
    curr_date = execution_date.strftime('%m%d%Y')
    name_of_file = f'patbatch_{curr_date}.csv'
    upload_to_bucket(file_path, s3, 'inputs/'+name_of_file)
