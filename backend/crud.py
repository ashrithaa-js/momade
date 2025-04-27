from sqlalchemy import case
from sqlalchemy.orm import Session
from models import User, Order
from schemas import OrderCreate, UserCreate
from passlib.context import CryptContext
from datetime import date, datetime, time, timedelta
import random

# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash password
def hash_password(password: str):
    return pwd_context.hash(password)

# Verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Create a new user
def create_user(db: Session, user: UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = User(
        username=user.username,
        name=user.name,
        phone_number=user.phone_number,
        password=hashed_pw,
        role=user.role if user.role else "customer"
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get user by username
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# Generate and store OTP
def generate_otp(db: Session, phone_number: str) -> str:
    otp = str(random.randint(100000, 999999))  # Generate 6-digit OTP
    expiry_time = datetime.utcnow() + timedelta(minutes=5)  # Valid for 5 min
    
    user = db.query(User).filter(User.phone_number == phone_number).first()
    
    if user:
        user.otp = otp
        user.otp_expires_at = expiry_time
        print(f"DEBUG: Before commit - OTP: {user.otp}, Expires At: {user.otp_expires_at}")  # Debugging
        db.commit()
        db.refresh(user)
        print(f"DEBUG: After commit - OTP: {user.otp}, Expires At: {user.otp_expires_at}")  # Debugging

    return otp

# Verify OTP
def verify_otp(db: Session, phone_number: str, otp_code: str):
    user = db.query(User).filter(User.phone_number == phone_number, User.otp == otp_code).first()
    if user and user.otp_expires_at > datetime.utcnow():
        user.is_verified = True
        user.otp = None
        db.commit()
        return True
    return False


def get_sorted_orders(db: Session):
    priority_order = case(
        (Order.order_status == 'Pending', 1),
        (Order.order_status == 'Confirmed', 2),
        (Order.order_status == 'Delivered', 3),
        (Order.order_status == 'Cancelled', 4),
        else_=5
    )

    return db.query(Order).order_by(priority_order).all()

def is_order_deadline_valid(delivery_date: date, package_type: str) -> bool:
    """
    Checks if the order is placed before the deadline.
    - Lunch: Must be ordered by 5 PM the previous day.
    - Dinner: Must be ordered by 2 PM the same day.
    """
    now = datetime.now()
    
    if package_type == "Lunch":
        deadline = datetime.combine(delivery_date, time(17, 0))  # 5 PM previous day
        return now < deadline
    elif package_type == "Dinner":
        deadline = datetime.combine(delivery_date, time(14, 0))  # 2 PM same day
        return now < deadline
    return True  # No deadline for Breakfast

def create_order(db: Session, user_id: int, order_data: OrderCreate):
    """
    Places an order if it meets the deadline criteria.
    """
    from models import Package  # Import here to prevent circular import

    package = db.query(Package).filter(Package.package_id == order_data.package_id).first()
    if not package:
        return {"error": "Package not found"}

    if not is_order_deadline_valid(order_data.delivery_date, package.package_type):
        return {"error": "Order deadline has passed. Please choose another day."}

    new_order = Order(
        user_id=user_id,
        package_id=order_data.package_id,
        delivery_date=order_data.delivery_date,
        order_status="Pending"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order