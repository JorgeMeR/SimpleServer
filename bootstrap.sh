#!/bin/sh

export FLASK_APP=./servidor/principal.py

pipenv run flask --debug run -h 0.0.0.0
