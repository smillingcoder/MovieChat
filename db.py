import sqlite3

DB_PATH = "movies.db"

def connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def database_setup():
    conn=connection()
    c=conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS Final_Table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER UNIQUE NOT NULL,
        genres TEXT,
        release_date TEXT,
        title TEXT,
        vote_average REAL,
        overview TEXT,
        poster_path TEXT,
        DOI DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """


    c.execute(query)

    conn.commit()
    c.close()
    connection().close()
    print("database present")









