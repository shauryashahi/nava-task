from pydantic import BaseModel, EmailStr
from datetime import datetime

class OrganizationCreate(BaseModel):
    name: str
    admin_email: EmailStr
    admin_password: str

class OrganizationResponse(BaseModel):
    id: int
    name: str
    db_name: str
    created_at: datetime

    class Config:
        from_attributes = True