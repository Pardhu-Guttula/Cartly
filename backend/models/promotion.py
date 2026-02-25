from sqlalchemy import Column, Integer, String, Date, Float, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Epic Title: Develop Frontend Interface for Promotions

Base = declarative_base()

class Promotion(Base):
    __tablename__ = 'promotions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(20), nullable=False, unique=True)
    description = Column(String(255), nullable=False)
    discount_amount = Column(Float, nullable=False)
    expiration_date = Column(Date, nullable=False)
    
    discounts = relationship("Discount", back_populates="promotion")
    
    __table_args__ = (
        Index('ix_code', 'code'),
    )