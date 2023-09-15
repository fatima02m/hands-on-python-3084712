import csv #allows to read data
import json
from pprint import pprint

#Einstein is a dictionary
EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}
#json.dumps creates a string 
einstein_json = json.dumps(EINSTEIN)
back_to_dict = json.loads(einstein_json)
print(einstein_json)
print('---------')
pprint(back_to_dict)

#creates a list of python dictionaries
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

#use .dump (singular)for files
with open("laureates.json", "w") as f:
    json.dump(laureates, f, indent=2)
