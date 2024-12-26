import pandas as pd  #for dataframe manipulation

from etls.patient_generator import  generate_patient


def create_dataframe():
    #1.the randomizer will have 10000 patients to simulate 'big data'
    #2.1/4 of the total will focus on each of the parameters
    #3.I will do 80% of each of the subgroups are normal, 8% are elevated, 8% are in serious condition
    #and 4% will have a mix.
        #2000, 200, 200, 100
    #4.Should I add mixed conditions? (e.g. fever and diabetic)
    patients = []

    for i in range(8000):
        p = generate_patient('n','n','n','n',)
        patients.append(p)

    for i in range(200):
        p = generate_patient('h1','n','n','n',)
        patients.append(p)
    for i in range(200):
        p = generate_patient('h2','n','n','n',)
        patients.append(p)

    for i in range(200):
        p = generate_patient('n','h1','n','n',)
        patients.append(p)
    for i in range(200):
        p = generate_patient('n','h2','n','n',)
        patients.append(p)

    for i in range(200):
        p = generate_patient('n','n','high','n',)
        patients.append(p)
    for i in range(200):
        p = generate_patient('n','n','extreme','n',)
        patients.append(p)

    for i in range(200):
        p = generate_patient('n','n','n','e',)
        patients.append(p)
    for i in range(200):
        p = generate_patient('n','n','n','d',)
        patients.append(p)

    for i in range(100):
        p = generate_patient('h2','n','n','d',)
        patients.append(p)
    for i in range(100):
        p = generate_patient('n','h2','n','d',)
        patients.append(p)
    for i in range(100):
        p = generate_patient('n','n','extreme','d',)
        patients.append(p)
    for i in range(100):
        p = generate_patient('h2','h1','mild','d',)
        patients.append(p)

    #constructor converts list to dataframe
        #constructor checks if the column name matches a key from the dictionary, so it is spelling specific.
        #If it matches, it retrieves the value
    df = pd.DataFrame(patients,
                      columns=['First_name', 'Last_name', 'Date_of_birth', 'Age', 'Phone_number', 'SSN', 'Systolic(BP)',
                               'Diastolic(BP)', 'Oxygen_saturation', 'Heart_rate', 'Respiratory_rate', 'Temperature',
                               'Glucose_levels'])

    # print(df.shape) # tuple-form of dataframe, or (rows, columns)
    # print(df)
    return df

def load_dataframe(df:pd.DataFrame, file_path):
    df.to_csv(file_path, index=False)

