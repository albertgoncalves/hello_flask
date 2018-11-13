#!/usr/bin/env python3

from datetime import datetime as dt
import json

from flask import Flask
from flask.app import request as flask_request
from sqlalchemy import create_engine

from api_demo_funs import check_type
from api_demo_funs import sanitize_id

# side-effects
def echo_id(item_id):
    user_agent = flask_request.headers.get('User-Agent', None)
    sanitize   = check_type(item_id, int, 0)
    rtn_str    = "item id: {}<br>user_agent: {}<br>now: {}"
    return rtn_str.format(sanitize, user_agent, dt.now())

def app_init(flask_app):
    def app_wrapper(rule, endpoint, view_func):
        flask_app.add_url_rule(rule, endpoint, view_func)
    return app_wrapper

def run_query(db_conn, query_str):
    conn = db_conn.connect()
    return conn.execute(query_str)

def query(db_conn):
    def qry():
        qry_str = "SELECT * FROM tbl1;"
        data    = run_query(db_conn, qry_str)
        result  = \
            {"data": [dict(zip(tuple(data.keys()), i)) for i in data.cursor]}
        return json.dumps(result)
    return qry

def insert(db_conn):
    def ins(item_id):
        user_agent = flask_request.headers.get('User-Agent', None)
        ins_char = sanitize_id(item_id)

        ins_str = """INSERT INTO tbl1(item_id, header) VALUES({}, '{}')
                  """.format(ins_char, user_agent)
        run_query(db_conn, ins_str)

        rtn_str = "' <strong>{}</strong> '<br>at <em>{}</em>"
        return rtn_str.format(ins_str, dt.now())
    return ins

# do block
def main():
    app      = Flask(__name__)
    app_cons = app_init(app)
    db_conn  = create_engine('sqlite:///hello.db')

    pages = [ ("/echo/<item_id>"  , "echo_id", echo_id        )
            , ("/query"           , "query"  , query(db_conn) )
            , ("/insert/<item_id>", "insert" , insert(db_conn))
            ]

    for page in pages:
        app_cons(*page)

    app.run(debug=True, port=5002, host='192.168.1.52')

if __name__ == "__main__":
    main()
