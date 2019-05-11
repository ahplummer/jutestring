# Inroduction
This is a simple URL shortening service, specifically made to return in a format convenient for Slack.

## Setting Up
* Create a virtualenv: `virtualenv -python=python3 .venv`
* Activate virtualenv: `. .venv/bin/activate`
* Grab dependencies: `pip install -r requirements.txt`

## Test
* Run tests: `python -m pytest -s test/ `

## Run locally
* Set BASEURL and PORT env vars.

## Run as docker 
* Set environment variable for BASEURL, PORT
```
export BASEURL=<your http: address with trailing slash>
export PORT=<your port>
```
* Build docker image:
```
docker-compose up -d --build
```
* Run docker image via docker-compose:
```
docker-compose exec jutestring python3 flaskdriver.py
```
* Test with curl
```
curl --request POST --data text=http://www.google.com  http://127.0.0.1:5555/add
 
```
...then try curling the returned link, you should get a 302 redirect.
