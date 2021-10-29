from sqlalchemy import Column, BigInteger, String
from sqlalchemy.sql.functions import user
from settings import db

class User(db.Model):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True)
    username = Column(String(32), unique=True)

    def __init__(self, username):
        self.username = username