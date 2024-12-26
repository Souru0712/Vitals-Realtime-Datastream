import os
import csv
import json

path_to_output = 'C:/Users/oscar/PycharmProjects/Health_Data_Engineering/data/output'
csv_directory = os.listdir(path_to_output)
csv_files = [file for file in csv_directory if file.endswith(".csv")]

for file in csv_files:
    csv_file_path = f'{path_to_output}/{file}'
    print(csv_file_path)

    with open(csv_file_path, mode="r", encoding="utf-8") as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            json_object = json.dumps(row, indent=4)
            print(json_object)
