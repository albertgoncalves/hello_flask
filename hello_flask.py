#!/usr/bin/env python3

# via https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq
# and http://flask.pocoo.org/docs/1.0/api/#flask.Flask.add_url_rule
# and http://www.sqlitetutorial.net/sqlite-sample-database/

import json
from datetime import datetime as dt

from flask import Flask
from sqlalchemy import create_engine

# pure functions
def index():
    return "Hello, index!"

def blob(key):
    blb = { "hello": "world"
          , "foo"  : "bar"
          }
    if key in blb.keys():
        value = blb[key]
    else:
        value = "<strong>{}</strong> not in the blob!".format(key)

    return "{}<br>{}".format(json.dumps(blb), value)

def now():
    return str(dt.now())

def username(name):
    return "Hello, {}!".format(name.title())

# ...pure?
def check_type(input_val, output_type, default_val):
    try:
        val = output_type(input_val)
    except ValueError:  # read: TypeError !
        val = default_val
    return val

# side-effects
def app_init(flask_app):
    def app_wrapper(rule, endpoint, view_func):
        flask_app.add_url_rule(rule, endpoint, view_func)
    return app_wrapper

def run_query(db_conn, query_str):
    conn = db_conn.connect()
    return conn.execute(query_str)

def query(db_conn):
    # $ sqlite3 chinook.db
    # sqlite> .tables
    # sqlite> PRAGMA table_info(employees);
    def limiter(limit):
        sanitize = check_type(limit, int, 0)
        qry_str  = """ SELECT FirstName, LastName
                       FROM employees LIMIT {};
                   """.format(sanitize)
        data     = run_query(db_conn, qry_str)
        result   = \
            {"data": [dict(zip(tuple(data.keys()), i)) for i in data.cursor]}
        return json.dumps(result)
    return limiter

# do block
def main():
    app      = Flask(__name__)
    app_cons = app_init(app)
    db_conn  = create_engine('sqlite:///chinook.db')

    pages = [ ("/"             , "index"   , index         )  # http://localhost:5002/
            , ("/index"        , "index"   , index         )  # http://localhost:5002/index
            , ("/blob/<key>"   , "blob"    , blob          )  # http://localhost:5002/blob/foo
            , ("/now"          , "now"     , now           )  # http://localhost:5002/now
            , ("/user/<name>"  , "username", username      )  # http://localhost:5002/user/albert
            , ("/query/<limit>", "query"   , query(db_conn))  # http://localhost:5002/query/4
            ]

    for page in pages:
        app_cons(*page)

    app.run(debug=True, port=5002)

if __name__ == "__main__":
    main()
