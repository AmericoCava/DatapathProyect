from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text, Float, BigInteger
from utils.db import Base
class Enunciado1(Base):
    __tablename__ = "enunciado1"
    index = Column(Integer, primary_key=True)
    customer_id = Column(Text)
    customer_fname = Column(Text)
    customer_lname = Column(Text)
    customer_email = Column(Text)
    quantity_item_total = Column(BigInteger)
    total = Column(BigInteger)