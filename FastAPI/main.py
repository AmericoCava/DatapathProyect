from utils.db import SessionLocal, engine, get_database_session
from models.enunciado1 import Enunciado1
from queries.enunciado1 import *
from api import app
from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session


@app.get("/enunciado1")
def read_enunciado(request: Request, db: Session = Depends(get_database_session)):
    records = read_query_enunciado(db)
    return records

@app.get("/enunciado1/{index}")
def read_enunciado_by_index(index,request: Request, db: Session = Depends(get_database_session)):
    records = read_query_enunciado_by_index(db,index)
    return records