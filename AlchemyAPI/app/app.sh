#!/bin/sh

pip install bottle==0.12.13 psycopg2==2.7.3.2 redis==2.10.5
pip install flask
pip install flask-sqlalchemy
pip install flask-jwt-extended
pip install flask-restful
python -u app.py