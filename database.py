from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Define the Archetypal Schema (◦A)
Base = declarative_base()

class TableA(Base):
    __tablename__ = 'table_a'
    id = Column(Integer, primary_key=True)
    value = Column(String)
    integrity_score = Column(Integer)

# Initialize the Lithic Connection
# Defaulting to local SQLite for immediate stabilization
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./mlaos_persistence.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Substrate Fossilized: table_a created.")

if __name__ == "__main__":
    init_db()
