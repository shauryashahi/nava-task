from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from .core.config import settings

engine = create_engine(settings.MASTER_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_org_database(org_name: str) -> str:
    db_name = f"org_{org_name.lower().replace(' ', '_').replace('-', '_')}"
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="db"
        )
        conn.autocommit = True
        cur = conn.cursor()
        
        # Create new database
        cur.execute(f"CREATE DATABASE {db_name}")
        
        cur.close()
        conn.close()
        return db_name
    except Exception as e:
        raise Exception(f"Failed to create organization database: {str(e)}")