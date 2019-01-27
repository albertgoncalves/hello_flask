#!/usr/bin/env python3

# via https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq
# and http://flask.pocoo.org/docs/1.0/api/#flask.Flask.add_url_rule
# and http://www.sqlitetutorial.net/sqlite-sample-database/

from datetime import datetime as dt
import json

from flask import Flask
from sqlalchemy import create_engine


def index():
    return "Hello, index!"


def blob(key):
    blb = \
        { "hello": "world"
        , "foo": "bar"
        , "food": "barf"
        }

    if key in blb.keys():
        r = blb[key]
    else:
        r = "<strong>{}</strong> not in the blob!".format(key)

    return "{}<br>{}".format(json.dumps(blb), r)


def now():
    return str(dt.now())


def username(name):
    return "Hello, {}!".format(name.title())


def check_type(input_val, output_type, default_val):
    try:
        val = output_type(input_val)
    except (ValueError, TypeError):
        val = default_val
    return val


def app_init(flask_app):
    def app_wrapper(rule, endpoint, view_func):
        flask_app.add_url_rule(rule, endpoint, view_func)

    return app_wrapper


def run_query(db, query):
    return db.connect().execute(query)


def query(db):
    # $ sqlite3 chinook.db
    # sqlite> .tables
    # sqlite> PRAGMA table_info(employees);
    def inject(n):
        qry = """
            SELECT FirstName, LastName FROM employees LIMIT {};
        """.format(check_type(n, int, 0))

        data = run_query(db, qry)

        result = \
            {"data": [dict(zip(tuple(data.keys()), i)) for i in data.cursor]}

        return json.dumps(result)

    return inject


def main():
    app = Flask(__name__)
    app_cons = app_init(app)
    db = create_engine('sqlite:///chinook.db')

    pages = \
        [ ("/", "index", index)                   # http://localhost:5002/
        , ("/index", "index", index)              # .../index
        , ("/blob/<key>", "blob", blob)           # .../blob/foo
        , ("/now", "now", now)                    # .../now
        , ("/user/<name>", "username", username)  # .../user/albert
        , ("/query/<n>", "query", query(db))      # .../query/4
        ]

    for page in pages:
        app_cons(*page)

    app.run(debug=True, port=5002)


if __name__ == "__main__":
    main()
