import sqlite3

def connect():
    return sqlite3.connect("snakes.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS snakes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        scientific_name TEXT,
        venomous TEXT,
        average_length REAL,
        habitat TEXT,
        region TEXT,
        diet TEXT,
        conservation_status TEXT
    )
    """)

    conn.commit()
    conn.close()