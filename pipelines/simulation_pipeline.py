from datetime import datetime

from etls.patient_etl import create_dataframe, load_dataframe
from etls.transform_data import transform_data
from utils.constants import OUTPUT_PATH


def simulation_pipeline(execution_date:datetime):
    curr_date = execution_date.strftime('%m%d%Y')

    name_of_file = f'patbatch_{curr_date}.csv'  #patient batch with current date
    file_path = f'{OUTPUT_PATH}/{name_of_file}'

    #extraction
    patients_df = create_dataframe()

    #transformation
    transformed_df = transform_data(patients_df)

    #load
    load_dataframe(transformed_df, file_path)

    return file_path

