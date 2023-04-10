import json

final_global = []


with open("global_therapy_list.json", "r") as f:
    data1 = json.load(f)

with open("alpaca_data.json", "r") as f:
    data2 = json.load(f)

for item in data1:
    final_global.append(item)

for item in data2:
    final_global.append(item)

with open("alpaca_counseling_merged.json", "w") as f:
    json.dump(final_global, f)