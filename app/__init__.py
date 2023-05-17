"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7nk5269vf5qb9jr9g-a.oregon-postgres.render.com",
        database="todo_1d7p",
        user="todo_1d7p_user",
        password="Fz9ETGX5ANBlXwEeQXFoI1xg4nkCHtnT")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
