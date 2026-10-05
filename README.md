# BrewSite

Emily Barron — ICT 362 Python Programming — Project 1

A Flask/Jinja website with a home page containing three local SVG images and a New Mexico brewery directory.

## Run on macOS

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m flask --app app run --port 5000
```

Open http://127.0.0.1:5000/home and http://127.0.0.1:5000/brewery. If port 5000 is in use, use 5001. Stop with Control+C.

## Data and images

Brewery data comes from https://api.openbrewerydb.org/v1/breweries?by_state=new_mexico&per_page=8. A saved October 2, 2026 snapshot is included for API outages. Names and addresses may change.

The three SVG illustrations are bundled locally; no third-party image hosting is required.

## Course scope

This implementation follows the written assignment requirements. Compare it with the four course videos before submission; their exact code and branch steps have not been verified.

Branches: development, staging, production. These are Git branches, not hosting environments.

Documentation: https://flask.palletsprojects.com/en/stable/quickstart/ and https://www.openbrewerydb.org/documentation
