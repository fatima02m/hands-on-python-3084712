import requests

# reading from online website that is formatted in json
response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

# gets the year number which is the #1 list item for each entry for 20 years
last_twenty_years = response.json()[1][:20]

for year in last_twenty_years:
    # limites the display value
    display_width = year["value"] // 10_000_000
    print(year["date"], "=" * display_width)
   # print(f'{year["date"]}: {year["value"]}',"=" * display_width)
