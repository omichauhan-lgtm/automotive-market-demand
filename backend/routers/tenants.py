from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, auth
from database import get_db

router = APIRouter(
    prefix="/tenants",
    tags=["tenants"]
)

@router.get("/me", response_model=schemas.Tenant)
def read_current_tenant(current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    tenant = db.query(models.Tenant).filter(models.Tenant.id == current_user.tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return tenant
