from typing import Annotated, Literal
from pydantic import BaseModel, StringConstraints
from datetime import date, datetime

# Base User Schema
PhoneNumberType = Annotated[str, StringConstraints(min_length=10, max_length=15)]

class UserBase(BaseModel):
    username: Annotated[str, StringConstraints(min_length=3, max_length=50)]
    password: Annotated[str, StringConstraints(min_length=6)]
    phone_number: PhoneNumberType  # Using the annotated type
    name: Annotated[str, StringConstraints(min_length=3, max_length=100)]
    role: Literal["customer", "cook", "admin"] = "customer"


# Schema for user creation (Signup)
class UserCreate(UserBase):
    password: str  # Password will be hashed later

# Schema for returning user data
class UserResponse(UserBase):
    user_id: int
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Schema for user login
class UserLogin(BaseModel):
    username: str
    password: str

# Schema for OTP verification
class OTPVerify(BaseModel):
    phone_number: str
    otp: str


class OrderCreate(BaseModel):
    package_id: int
    delivery_date: date  # The date when the meal should be delivered

# Order Response Schema
class OrderResponse(BaseModel):
    order_id: int
    user_id: int
    package_id: int
    order_date: datetime
    delivery_date: date
    order_status: str

    class Config:
        from_attributes = True