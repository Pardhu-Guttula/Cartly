from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Epic Title: Integrate multiple payment gateways

Base = declarative_base()

class PaymentGateway(Base):
    __tablename__ = 'payment_gateways'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    status = Column(String(50), nullable=False)