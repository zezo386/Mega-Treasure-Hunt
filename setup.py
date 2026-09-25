import sqlite3 as sq

def setup():
    conn = sq.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS highscores")

    cursor.execute("""CREATE TABLE highscores (
                   username TEXT NOT NULL,
                   score INTEGER DEFAULT 0
    )""")

    conn.commit()

if __name__ == "__main__":
    setup()