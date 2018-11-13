#!/usr/bin/env bash

if [ ! -f ./hello.db ]; then
    sqlite3 hello.db "CREATE TABLE tbl1(one VARCHAR(10), two SMALLINT);"
    sqlite3 hello.db "INSERT INTO tbl1 VALUES('hello!', 10);"
    sqlite3 hello.db "INSERT INTO tbl1 VALUES('goodbye', 20);"
fi
sqlite3 hello.db "SELECT * FROM tbl1;"
