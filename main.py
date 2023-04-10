import os
import json

for file in os.listdir("./"):
    if "company" in file:
        with open(f"./{file}", 'r') as f:
            data = json.load(f)

        # Count the number of elements in the list
        num_elements = len(data)

        # Print the result
        print(f'The JSON file contains {num_elements} elements.')