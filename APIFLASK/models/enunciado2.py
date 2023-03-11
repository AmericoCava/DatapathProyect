from utils.db import db

class Enunciado2 (db.Model):
    __tablename__ = 'enunciado2'
    index = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.Text)
    item_quantity = db.Column(db.BigInteger)
    total = db.Column(db.BigInteger)
    
    def to_dict(self):
        return {
            "category_name": self.category_name,
            "item_quantity": self.item_quantity,
            "total" : self.total
        }

