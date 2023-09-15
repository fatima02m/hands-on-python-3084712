import csv
from pprint import pprint

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}
#openning files
# using with doesnt leave file open for too long
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

#for each entery person, if their name is Einstein print their entire information
for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        break
