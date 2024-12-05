from pydantic import BaseModel, EmailStr, conint, validator
from datetime import datetime
from typing import List, Optional

# User Pydantic Models
class UserBase(BaseModel):
    name: str
    email: EmailStr  # Ensures valid email format

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    name: Optional[str] = None
    email: Optional[str] = None

class User(UserBase):
    id: int
    created_at: str  # This field should be a string

    @validator('created_at', pre=True, always=True)
    def format_datetime(cls, v):
        if isinstance(v, datetime):
            return v.isoformat()  # Convert datetime to string (ISO format)
        return v

    class Config:
        from_attributes = True  # Use 'from_attributes' instead of 'orm_mode'

# Order Pydantic Models
class OrderBase(BaseModel):
    product_name: str
    quantity: conint(gt=0)  # Ensures quantity is greater than 0

class OrderCreate(OrderBase):
    user_id: int

class OrderUpdate(OrderBase):
    product_name: Optional[str] = None
    quantity: Optional[int] = None

class Order(OrderBase):
    id: int
    user_id: int
    order_date: str  # This field should be a string

    @validator('order_date', pre=True, always=True)
    def format_datetime(cls, v):
        if isinstance(v, datetime):
            return v.isoformat()  # Convert datetime to string (ISO format)
        return v

    class Config:
        from_attributes = True  # Use 'from_attributes' instead of 'orm_mode'
