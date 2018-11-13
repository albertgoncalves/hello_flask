#!/usr/bin/env bash

if [ ! -f ./hello.db ]; then
    sqlite3 hello.db "CREATE TABLE tbl1(id SMALLINT, ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL);"
    sqlite3 hello.db "INSERT INTO tbl1(id) VALUES(1);"
    sleep 1s
    sqlite3 hello.db "INSERT INTO tbl1(id) VALUES(2);"
    sleep 1s
    sqlite3 hello.db "INSERT INTO tbl1(id) VALUES(3);"
fi
sqlite3 hello.db "SELECT * FROM tbl1;"
