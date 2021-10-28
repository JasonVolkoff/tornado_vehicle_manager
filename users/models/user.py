from sqlalchemy import Column, BigInteger, String
from settings import db

class User(db.Model):
    id = Column(BigInteger, primary_key=True)
    username = Column(String(32), unique=True)