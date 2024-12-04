from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...api.deps import get_db
from ...models.admin import Admin
from ...schemas.admin import AdminLogin, Token
from ...core.security import verify_password, create_access_token

router = APIRouter()

@router.post("/login", response_model=Token)
def login_admin(admin_data: AdminLogin, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.email == admin_data.email).first()
    if not admin or not verify_password(admin_data.password, admin.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    access_token = create_access_token(data={"sub": admin.email, "org_id": admin.org_id})
    return {"access_token": access_token, "token_type": "bearer"}