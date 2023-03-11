from models.enunciado3 import Enunciado3

from utils.db import db

def get_enunciado3():
    try:
        enunciados = [enunciado.to_dict() for enunciado in Enunciado3.query.all()]
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