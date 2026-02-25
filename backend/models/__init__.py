from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from backend.models.transaction import Base as TransactionBase
from backend.models.payment_gateway import Base as PaymentGatewayBase

# Epic Title: Integrate multiple payment gateways

DATABASE_URL = 'mysql+mysqlconnector://username:password@localhost/mydatabase'

engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session_factory = scoped_session(SessionLocal)

def init_db():
    TransactionBase.metadata.create_all(bind=engine)
    PaymentGatewayBase.metadata.create_all(bind=engine)