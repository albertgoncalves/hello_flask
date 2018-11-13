#!/usr/bin/env bash

if [ ! -f ./hello.db ]; then
    sqlite3 hello.db "CREATE TABLE tbl1(id INTEGER PRIMARY KEY, item_id SMALLINT, header VARCHAR(100), ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL);"
    sqlite3 hello.db "INSERT INTO tbl1(item_id, header) VALUES(null, null);"
fi
sqlite3 hello.db "SELECT * FROM tbl1;"
