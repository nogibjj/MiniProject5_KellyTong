import sqlite3
import csv

def load(file_path="Auto.csv"):
    """Transforms and Loads data into the local SQLite3 database"""
    
    with open(file_path, 'r', newline='') as f:
        csv_reader = csv.reader(f, delimiter=';')
        next(csv_reader)  
        payload = [row for row in csv_reader if row]  


    for row in payload:
        if len(row) != 9:
            print(f"Incorrect number of fields in row: {row}")

    conn = sqlite3.connect('AutoDB.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS AutoDB")
    
    # Create table query split for better readability
    create_table_query = (
        "CREATE TABLE AutoDB ("
        "Brand TEXT)"
    )
    c.execute(create_table_query)
    
    # Insert data query
    insert_data_query = (
        "INSERT INTO AutoDB (Brand) VALUES (?)"
    )
    c.executemany(insert_data_query, payload)
    
    conn.commit()
    conn.close()
    return "AutoDB.db"
