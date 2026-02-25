from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from backend.models.performance_metric import PerformanceMetric
from backend.models.user_behavior import UserBehavior

# Epic Title: Develop PostgreSQL Database for Performance Metrics

DATABASE_URL = 'postgresql+psycopg2://username:password@localhost/mydatabase'

engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session_factory = scoped_session(SessionLocal)

def init_db():
    PerformanceMetric.metadata.create_all(bind=engine)
    UserBehavior.metadata.create_all(bind=engine)

### Services