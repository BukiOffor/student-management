import sqlite3

connection = sqlite3.connect('database.db')

# read the created schema.sql file and create a database
with open('course_schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
connection.close()

