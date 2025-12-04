from pydantic import BaseModel
from typing import Optional, List

class TenantBase(BaseModel):
    name: str

class TenantCreate(TenantBase):
    pass

class Tenant(TenantBase):
    id: int
    plan: str
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    tenant_name: str  # Create tenant during signup for simplicity

class UserLogin(UserBase):
    password: str

class User(UserBase):
    id: int
    tenant_id: int
    role: str
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
