#Since we have to finish with structured data, we can think of data cleaning as a way to prevent
#or take care of any human error such as typo's (incorrect, corrupted, or formatted not common in standards),
# duplicates, and nulls
import pandas as pd
import numpy as np
import re

#Thus this program attempts to establish a template to force data cleaning to retrieve correct, standardized data


# PANDAS
#.astype() // to tranform data type
#.drop() //drop columns
    #drop_duplicates(
#.read_csv // outputs entire csv database
#[column].str.strip()
    #lstrip()
    #rstrip()
#[column].str.replace('[regular expression]')
#apply(np functions)
    #apply(lambda x :

# NUMPY
# .where() // to return two values based on the condition
def transform_data(df:pd.DataFrame):
    df = transform_date(df)
    df = transform_phone(df)
    df = transform_SSN(df)

    return df

def transform_date(df:pd.DataFrame):
    #assuming the dob is in the format mm-dd-yyyy
    df['Date_of_birth'] = df['Date_of_birth'].str.replace('[^0-9]', '', regex=True) #remove symbols

    #catch errors of dates that are unrealistic (mm = 13)

    df['Date_of_birth'] = df['Date_of_birth'].apply(lambda x: x[0:2] + '/' + x[2:4] + '/' + x[4:8])

    return df

def transform_phone(df:pd.DataFrame):
    df['Phone_number'] = df['Phone_number'].str.replace('[^0-9]', '', regex=True) #remove letters and symbols

    # retrieve the last ten digits //x[0:] starts from the left and the area code may have more than 1 digit
    df['Phone_number'] = df['Phone_number'].apply(lambda x: x[len(x)-10:len(x)])

    #standardize
    df['Phone_number'] = df['Phone_number'].apply(lambda x : '(' + x[0:3] + ')' +x[3:6] +'-' +x[6:10])
    return df

def transform_SSN(df:pd.DataFrame):
    df['SSN'] = df['SSN'].str.replace('[^0-9]', '', regex=True)

    df['SSN'] = df['SSN'].apply(lambda x : x[5-9])

    return df

def sample_test():
    patient1 = {'Phone_number': '+1(917)8085218',
                'Date_of_birth': '11~15~1967'}
    patient2 = {'Phone_number': '+191646/427-6509',
                'Date_of_birth': '12-25-1997'}

    list = []
    list.append(patient1)
    list.append(patient2)

    return pd.DataFrame(data=list, columns=['Phone_number', 'Date_of_birth'])


def test_phone(sample_df:pd.DataFrame):
    sample_df['Phone_number'] = sample_df['Phone_number'].astype('string') #object -> string
    sample_df['Date_of_birth'] = sample_df['Date_of_birth'].astype('string')

    print(sample_df['Phone_number'].dtypes)
    sample_df = transform_phone(sample_df)
    # print(sample_df)

    #print(sample_df['Date_of_birth'].dtypes)
    sample_df = transform_date(sample_df)
    print(sample_df)

# sample_df = sample_test()
# print(sample_df)
# test_phone(sample_df)