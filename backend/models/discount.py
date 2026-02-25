from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Epic Title: Store Promotion and Discount Data in PostgreSQL

Base = declarative_base()

class Discount(Base):
    __tablename__ = 'discounts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    discount_amount = Column(Float, nullable=False)
    promotion_id = Column(Integer, ForeignKey("promotions.id"), nullable=False)
    
    promotion = relationship("Promotion", back_populates="discounts")