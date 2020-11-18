"""
This file contains patterns sql ddl commands
"""
create_table_patrn_one = """
    CREATE TABLE test (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email text NOT NULL UNIQUE,
    joining_date datetime,
    salary REAL NOT NULL);
"""
create_table_patrn_two = """
    CREATE TABLE hardware (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL);
"""

