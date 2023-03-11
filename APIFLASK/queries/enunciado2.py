from models.enunciado2 import Enunciado2

from utils.db import db

def get_enunciado2():
    try:
        enunciados = [enunciado.to_dict() for enunciado in Enunciado2.query.all()]
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