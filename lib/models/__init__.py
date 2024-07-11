import sqlite3

CONN = sqlite3.connect('lib/models/data.db')
CURSOR = CONN.cursor()
