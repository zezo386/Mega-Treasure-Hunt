import sqlite3 as sq
import fastapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from pydantic import BaseModel

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

class addScore(BaseModel):
    username: str
    score: int

@app.get("/top10/")
def top10():
    try:
        conn = sq.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM highscores ORDER BY score DESC LIMIT 10")
        result = cursor.fetchall()
        result = [{"username":n[0],"score":n[1]} for n in result]

        return result
    except Exception as e:
        raise HTTPException(500, f"can not get the top 10, {e}")
    finally:
        conn.close()

@app.post("/add_score/")
def add_score(i: addScore):
    try:
        conn = sq.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO highscores (username, score) VALUES (?, ?)",(i.username,i.score))
        conn.commit()

        return {"details":"Added successfully"}
    except Exception as e:
        raise HTTPException(500, f"Could not add the new score, {e}")
    finally:
        conn.close()

@app.get("/top5pr/{username}")
def top5pr(username: str):
    try:
        conn = sq.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("SELECT score FROM highscores WHERE username = ?",(username,))
        result = cursor.fetchall()

        if not result:
            raise HTTPException(404, "user not found")
        return result[0]
    except HTTPException:
        raise HTTPException(404, "user not found")
    except Exception as e:
        raise HTTPException(500, f"an error occured, {e}")
    finally:
        conn.close()

