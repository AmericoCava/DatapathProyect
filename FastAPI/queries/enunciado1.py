from models.enunciado1 import Enunciado1


def read_query_enunciado(db):
    records = db.query(Enunciado1).all()
    return records

def read_query_enunciado_by_index(db, index):
    records = db.query(Enunciado1).filter(Enunciado1.index==index).first()
    return records