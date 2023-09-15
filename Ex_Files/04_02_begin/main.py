from flask import Flask

# instantiate flask object
app = Flask(__name__)

# define a route


@app.route("/")  # <-- called a decorator
def hello():
    return "Hello, World!"


app.run(debug=True)

# when you run this, opens a browser
# click the button at the bottom communication button thingy to open the browsser
