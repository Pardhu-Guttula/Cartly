# Epic Title: Integrate Promotion System with Order Management

from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from backend import db

class Order(db.Model):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    promotion_code = Column(String(50), nullable=True)
    final_amount = Column(DECIMAL(10, 2), nullable=False)

    user = relationship('User', back_populates='orders')

    def __init__(self, user_id: int, total_amount: float, promotion_code: str, final_amount: float):
        self.user_id = user_id
        self.total_amount = total_amount
        self.promotion_code = promotion_code
        self.final_amount = final_amount