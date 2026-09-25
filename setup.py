import sqlite3 as sq

def setup():
    conn = sq.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS highscores")

    cursor.execute("""CREATE TABLE highscores (
                   username TEXT NOT NULL,
                   score INTEGER NOT NULL DEFAULT 0,
                   difficulty TEXT NOT NULL DEFAULT "medium"
    )""")

    conn.commit()

if __name__ == "__main__":
    setup()