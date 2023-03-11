from models.enunciado4 import Enunciado4

from utils.db import db

def get_enunciado4():
    try:
        enunciados = [enunciado.to_dict() for enunciado in Enunciado4.query.all()]
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