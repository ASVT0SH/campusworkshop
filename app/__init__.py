"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq4gndvk4rjsv9kro0-a.oregon-postgres.render.com",
        database="todo_95eg",
        user="root",
        password="da3gZcBCwQ5JrKs5nPc0UB6iKFug3G8C")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
