from utils.db import db

class Enunciado4 (db.Model):
    __tablename__ = 'enunciado4'
    index = db.Column(db.Integer, primary_key=True)
    customer_city = db.Column(db.Text)
    product_name = db.Column(db.Text)
    quantity = db.Column(db.BigInteger)
    total = db.Column(db.Float)
    
    def to_dict(self):
        return {
            "customer_city": self.customer_city,
            "product_name": self.product_name,
            "quantity": self.quantity,
            "total": self.total
        }

