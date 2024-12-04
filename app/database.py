from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from .core.config import settings

engine = create_engine(
    settings.MASTER_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_org_database(org_name: str) -> str:
    db_name = f"org_{org_name.lower().replace(' ', '_').replace('-', '_')}.db"
    db_path = f"sqlite:///./{db_name}"
    
    # Create new SQLite database file
    org_engine = create_engine(db_path)
    Base.metadata.create_all(bind=org_engine)
    
    return db_name