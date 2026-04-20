from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import os

Base = declarative_base()

class Sovereign(Base):
    __tablename__ = 'sovereigns'
    id = Column(Integer, primary_key=True)
    handle = Column(String, unique=True)
    clearance_tier = Column(Integer, default=1) 
    last_manifestation = Column(DateTime, default=datetime.datetime.utcnow)
    empathy_baseline = Column(Integer, default=100)

class TableA(Base):
    __tablename__ = 'table_a'
    id = Column(Integer, primary_key=True)
    value = Column(String)
    integrity_score = Column(Integer)

# USE AN ABSOLUTE PATH TO PREVENT DUALITY
DB_PATH = os.path.expanduser("~/mlaos_persistence.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
