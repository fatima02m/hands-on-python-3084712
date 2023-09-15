import csv
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

# @app.route converts the function's return value into an HTTP response to be displayed by an HTTP client


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate_list():
    # template found in templates/laureate.html
    results = []
    if not request.args.get("surname"):
        return jsonify(results)

    # creates a variable for what the user searches, its running constantly, get the sring using request.arg.get
    search_string = request.args.get("surname").lower().strip()

    for laureate in laureates:
        if search_string in laureate["surname"].lower():
            results.append(laureate)

    return jsonify(results)
# formats into json and returns the results


app.run(debug=True)
