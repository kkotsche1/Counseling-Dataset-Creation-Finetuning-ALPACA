import os
import json

json_files = [f for f in os.listdir('./') if "company" in f and "json" in f]

# Create an empty list to store the data from all files
data = []

# Iterate through each JSON file
for file in json_files:
    with open(os.path.join('./', file), 'r') as f:
        # Load the JSON data from the file
        json_data = json.load(f)
        for data_point in json_data:
        # Append the JSON data to the list
            data.append(data_point)
    print(len(data))
    print(file)
# Write the combined JSON data to a new file
with open('./company_combined_file.json', 'w') as f:
    json.dump(data, f)
