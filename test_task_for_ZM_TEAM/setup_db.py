import sqlite3
from os import path
from typing import List
from datetime import datetime


path_to_dir = path.dirname(__file__)
path_to_db = path.join(path_to_dir, "Profile.db")

CREATE_TABLE = """
DROP TABLE IF EXISTS 'Cookie Profile';
CREATE TABLE 'Cookie Profile' (
    id INTEGER PRIMARY KEY NOT NULL,
    datetime_of_creation TIMESTAMP NOT NULL,
    cookie TEXT,
    last_enter TIMESTAMP,
    counter INTEGER
);
"""


def create_table():
    with sqlite3.connect(path_to_db) as conn:
        cursor = conn.cursor()
        cursor.executescript(CREATE_TABLE)


def prepare_table():
    with sqlite3.connect(path_to_db) as conn:
        cursor = conn.cursor()
        cursor.executescript(CREATE_TABLE)

        users: List = [
            (u_in, datetime.now(), 'NULL', 'NULL', 'NULL') for u_in in range(1, 16)
        ]

        cursor.executemany("""
        INSERT INTO 'Cookie Profile' (id, datetime_of_creation, cookie, last_enter, counter)
        VALUES (?, ?, ?, ?, ?); 
        """, users)


if __name__ == "__main__":
    prepare_table()
