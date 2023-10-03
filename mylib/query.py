"""Query the database"""

import sqlite3


def query():
    """Query the database for the top 5 rows of AutoDB table"""
    conn = sqlite3.connect("AutoDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AutoDB LIMIT 5")
    print("Top 5 rows of AutoDB table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"
