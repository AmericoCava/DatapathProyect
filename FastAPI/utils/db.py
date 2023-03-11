from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
DATABASE_CONNECTION = 'mysql://root:Americo27#@127.0.0.1/retail?charset=utf8'
engine = create_engine(DATABASE_CONNECTION)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()