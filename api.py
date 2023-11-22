"""API with FastAPI."""

from fastapi import FastAPI
from pydantic import BaseModel

from calculator import calculate

app = FastAPI()

@app.get("/get_user")
def load_questions():
    return "gh"