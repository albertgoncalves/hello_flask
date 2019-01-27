#!/usr/bin/env python3

from datetime import datetime as dt
import json

from flask import Flask
from flask.app import request as flask_request
from sqlalchemy import create_engine

from funs import check_type
from funs import local_ip
from funs import sanitize_id


def user_agent_headers():
    return "User-Agent", None


def echo_id(item_id):
    user_agent = flask_request.headers.get(*user_agent_headers())
    sanitize = check_type(item_id, int)
    r = "item id: {}<br>user_agent: {}<br>now: {}"

    return r.format(sanitize, user_agent, dt.now())


def app_init(flask_app):
    def app_wrapper(rule, endpoint, view_func):
        flask_app.add_url_rule(rule, endpoint, view_func)

    return app_wrapper


def run_query(db, query):
    return db.connect().execute(query)


def query(db_conn):
    def inject():
        query = "SELECT * FROM qrs;"
        data = run_query(db_conn, query)
        result = \
            {"data": [dict(zip(tuple(data.keys()), i)) for i in data.cursor]}

        return json.dumps(result)

    return inject


def insert(db):
    def inject(item_id):
        user_agent = flask_request.headers.get(*user_agent_headers())

        insert = """
            INSERT INTO qrs(item_id, header) VALUES({}, '{}')
        """.format(sanitize_id(item_id), user_agent)

        run_query(db, insert)

        r = "' <strong>{}</strong> '<br>at <em>{}</em>"
        return r.format(insert, dt.now())

    return inject


def main():
    app = Flask(__name__)
    app_cons = app_init(app)
    db = create_engine("sqlite:///qr.db")

    pages = \
        [ ("/echo/<item_id>", "echo_id", echo_id)
        , ("/query", "query", query(db))
        , ("/insert/<item_id>", "insert", insert(db))
        ]

    for page in pages:
        app_cons(*page)

    app.run(debug=True, port=5002, host=local_ip())


if __name__ == "__main__":
    main()
