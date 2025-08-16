# Rocket.Chat Log Dashboard

![Python CI](https://github.com/Canepro/rocketchat-log-dashboard/actions/workflows/python.yml/badge.svg?branch=main)

A tiny Flask app serving a mock JSON logs endpoint and a Chart.js time-series UI.

## Run locally
`pwsh
python -m venv .venv
. .venv/Scripts/Activate.ps1
pip install -r requirements.txt
python app.py  # http://localhost:8000
`

## Deploy (example)
Any WSGI host works. For gunicorn:
`pwsh
pip install gunicorn
gunicorn -b 0.0.0.0:8000 app:app
`

## Notes
- Data is stubbed with random values for demo.
- Chart.js loaded via CDN.

## License
MIT