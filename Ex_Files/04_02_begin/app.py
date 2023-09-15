import csv
from flask import Flask, render_template, jsonify
# includes render function template that allows to render an HTML file

app = Flask(__name__)

with open("laureates.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

# index route


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate():
    return jsonify(laureates)


app.run(debug=True)

# creates webpage with all the laureates in a json format
