"""Query the database"""

import sqlite3


def query():
    """Query the database for the top 5 rows of Auto"""
    conn = sqlite3.connect("Auto.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AutoDB")
    print("Top 5 rows of Auto:")
    print(cursor.fetchall())
    conn.close()
    return "Success"
