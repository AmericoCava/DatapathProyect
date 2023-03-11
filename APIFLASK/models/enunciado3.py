from utils.db import db

class Enunciado3 (db.Model):
    __tablename__ = 'enunciado3'
    index = db.Column(db.Integer, primary_key=True)
    customer_city = db.Column(db.Text)
    category_name = db.Column(db.Text)
    
    def to_dict(self):
        return {
            "customer_city": self.customer_city,
            "category_name": self.category_name
        }

