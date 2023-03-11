from utils.db import db

class Enunciado1 (db.Model):
    __tablename__ = 'enunciado1'
    index = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Text)
    customer_fname = db.Column(db.Text)
    customer_lname = db.Column(db.Text)
    customer_email = db.Column(db.Text)
    quantity_item_total = db.Column(db.BigInteger)
    total = db.Column(db.Float)

    def to_dict(self):
        return {
            "id": self.customer_id,
            "customer_fname": self.customer_fname,
            "customer_lname" : self.customer_lname,
            "customer_email": self.customer_email,
            "quantity_item_total": self.quantity_item_total,
            "total": self.total
        }

