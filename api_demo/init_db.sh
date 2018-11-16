#!/usr/bin/env bash

if [ ! -f ./qr.db ]; then
    sqlite3 qr.db "
        CREATE TABLE qrs( id INTEGER PRIMARY KEY
                        , item_id SMALLINT
                        , header VARCHAR(100)
                        , ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                        );
    "
    sqlite3 qr.db "INSERT INTO qrs(item_id, header) VALUES(null, null);"
fi
sqlite3 qr.db "SELECT * FROM qrs;"
