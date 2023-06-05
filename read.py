import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
data_frame = pd.read_csv("C:/Users/being/OneDrive/Desktop/Revolve Solutions - Python Assignment (8)/python-assignment-level2-6ed53b4e828")



df2 = pd.read_json("C:/Users/being/OneDrive/Desktop/Revolve Solutions - Python Assignment (8)/python-assignment-level2-6ed53b4e828af18bc24b1770a3a3e3e70706e785/csv/transactions/d=2018-12-01/transactions.json", lines= True)
df2

from datetime import date

na = 0
str1 = "C:/Users/being/OneDrive/Desktop/Revolve Solutions - Python Assignment (8)/python-assignment-level2-6ed53b4e828af18bc24b1770a3a3e3e70706e785/csv/transactions/d=2018-12-01"
str2 = "/transactions.json"

date1 = date(2018, 12, 01)

while na !=91:

  date_string = "d=" + date1.strftime('%Y-%m-%d')
  path = str1 + date + str2

  #df2 = pd.read_json(path, lines= True)
  #df2 = pd.read_json(path, lines= True)

  # Specify the directory containing the JSON files
json_directory = "C:/Users/being/OneDrive/Desktop/Revolve Solutions - Python Assignment (8)/python-assignment-level2-6ed53b4e828af18bc24b1770a3a3e3e70706e785/csv/transactions"

# Create a list to store the JSON data sets
data_sets = []

# Get the list of JSON files in the directory
json_files = [f for f in os.listdir(json_directory) if f.endswith(".json")]

# Sort the JSON files alphabetically
json_files.sort()

# Iterate over the JSON files in sets of seven
for i in range(0, len(json_files), 7):
    # Create a new set of seven files
    json_set = json_files[i:i+7]
    set_data = []

    # Iterate over each file in the set
    for json_file in json_set:
        # Read the JSON data from each file
        file_path = os.path.join(json_directory, json_file)
        with open(file_path) as file:
            json_data = json.load(file)
            set_data.extend(json_data)

    # Add the set data to the list of data sets
    data_sets.append(set_data)

# Convert each data set to a DataFrame
data_frames = []
for data_set in data_sets:
    df = pd.DataFrame(data_set)
    data_frames.append(df)

# Concatenate the DataFrames
combined_df = pd.concat(data_frames, ignore_index=True)

# Select the desired features
selected_columns = ["customer_id", "product_id", "product_category", "purchase_count"]
df = combined_df[selected_columns]

# Print the resulting DataFrame
print(df)