import sqlite3 as sq
import fastapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from pydantic import BaseModel

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origin=["*"],
    allow_credentails=False,
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
    except HTTPException:
        raise HTTPException(500,"can not get the top 10")
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
    except HTTPException:
        raise HTTPException(500,"Could not add the new score")
    finally:
        conn.close()