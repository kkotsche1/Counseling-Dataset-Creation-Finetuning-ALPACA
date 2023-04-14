import json
from tqdm import tqdm

with open("counseling_data.json", "r") as f:
    data1 = json.load(f)

with open("company_combined_file.json", "r") as f:
    data2 = json.load(f)

final_global_json = []
for data in [data1, data2]:
    for element in tqdm(data):
        if "hello" not in element["instruction"] and "hello" not in element["output"] and "bye" not in element["instruction"] and "bye" not in element["output"]:
            instruction = element["instruction"].replace("-","").strip()
            output = element["output"].replace("-","").strip()

            final_global_json.append({
                "instruction":instruction,
                "input":"",
                "output": output
            })

with open('global_therapy_list.json', 'w') as f:
    json.dump(final_global_json, f)
