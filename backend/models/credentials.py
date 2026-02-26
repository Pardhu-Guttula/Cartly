# Epic Title: User Password Security

from backend import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class Credentials(db.Model):
    __tablename__ = 'credentials'

    id = Column(Integer, primary_key=True)
    password = Column(String(128), nullable=False)

    user = relationship("User", uselist=False, back_populates="credentials")

    def __init__(self, password: str):
        self.password = password