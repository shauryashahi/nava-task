from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    db_name = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    admins = relationship("Admin", back_populates="organization")