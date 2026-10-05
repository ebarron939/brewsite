"""BrewSite Flask application for ICT 362 Project 1."""
import json
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, render_template

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent


def load_breweries():
    """Get New Mexico breweries, using the saved snapshot if the API fails."""
    query = urlencode({"by_state": "new_mexico", "per_page": 8})
    request = Request(
        "https://api.openbrewerydb.org/v1/breweries?" + query,
        headers={"User-Agent": "BrewSite student project"},
    )
    try:
        with urlopen(request, timeout=5) as response:
            records = json.load(response)
        if not isinstance(records, list) or not records:
            raise ValueError("No brewery records returned")
        if not all(isinstance(row, dict) and row.get("name") for row in records):
            raise ValueError("Unexpected brewery records")
        source = "Open Brewery DB"
    except (URLError, TimeoutError, ValueError, OSError):
        records = json.loads((BASE_DIR / "data" / "breweries.json").read_text())
        source = "Saved Open Brewery DB snapshot from October 2, 2026"
    return records, source


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/brewery")
@app.route("/breweries")
@app.route("/Breweries")
def brewery():
    breweries, source = load_breweries()
    return render_template(
        "brewery.html", title="Breweries", breweries=breweries, source=source
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
