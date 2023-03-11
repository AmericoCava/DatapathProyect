from models.enunciado1 import Enunciado1

from utils.db import db

def get_enunciado1():
    try:
        enunciados = [enunciado.to_dict() for enunciado in Enunciado1.query.all()]
        payload = {
            "success": True,
            "data": enunciados
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    
    return payload