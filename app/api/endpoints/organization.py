from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...api.deps import get_db, get_current_admin
from ...database import create_org_database
from ...models.organization import Organization
from ...models.admin import Admin
from ...schemas.organization import OrganizationCreate, OrganizationResponse
from ...core.security import get_password_hash

router = APIRouter()

@router.post("/create", response_model=OrganizationResponse)
def create_organization(org_data: OrganizationCreate, db: Session = Depends(get_db)):
    if db.query(Organization).filter(Organization.name == org_data.name).first():
        raise HTTPException(status_code=400, detail="Organization already exists")
    
    try:
        db_name = create_org_database(org_data.name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    org = Organization(name=org_data.name, db_name=db_name)
    db.add(org)
    db.commit()
    db.refresh(org)
    
    admin = Admin(
        email=org_data.admin_email,
        password=get_password_hash(org_data.admin_password),
        org_id=org.id
    )
    db.add(admin)
    db.commit()
    
    return org

@router.get("/{organization_name}", response_model=OrganizationResponse)
def get_organization(
    organization_name: str,
    current_admin: Admin = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    org = db.query(Organization).filter(Organization.name == organization_name).first()
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
        
    if org.id != current_admin.org_id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized to access this organization"
        )
    
    return org
