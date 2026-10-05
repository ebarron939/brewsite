"""BrewSite initial Flask application."""
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
