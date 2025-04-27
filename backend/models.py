from sqlalchemy import Column, Integer, String, Boolean, DECIMAL, Enum, ForeignKey, TIMESTAMP, Date, BigInteger, func
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)  # Hashed passwords
    role = Column(Enum("customer", "cook", "admin", name="user_roles"), nullable=False, default="customer")
    name = Column(String(100), nullable=False)
    phone_number = Column(String(15), unique=True, nullable=False)
    otp = Column(String(6), nullable=True)
    otp_expires_at = Column(TIMESTAMP, nullable=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())

    orders = relationship("Order", back_populates="user")
    payments = relationship("Payment", back_populates="user")
    contact_messages = relationship("ContactMessage", back_populates="user")

# Package Model
class Package(Base):
    __tablename__ = "packages"

    package_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    package_type = Column(Enum('Breakfast', 'Lunch', 'Dinner'), nullable=False)
    package_name = Column(String(100), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

    # Relationship
    orders = relationship("Order", back_populates="package")

# Order Model
class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    package_id = Column(Integer, ForeignKey("packages.package_id"), nullable=False)
    order_date = Column(TIMESTAMP, default=datetime.utcnow)
    delivery_date = Column(Date, nullable=False)
    order_status = Column(Enum('Pending', 'Confirmed', 'Delivered', 'Cancelled'), default='Pending')

    # Relationships
    user = relationship("User", back_populates="orders")
    package = relationship("Package", back_populates="orders")
    payment = relationship("Payment", back_populates="order", uselist=False)

# Payment Model
class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    payment_method = Column(Enum('QR Code', 'Bank Account'), nullable=False)
    payment_status = Column(Enum('Pending', 'Completed', 'Failed'), default='Pending')
    zakpay_transaction_id = Column(String(100), nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    # Relationships
    order = relationship("Order", back_populates="payment")
    user = relationship("User", back_populates="payments")

# Contact Message Model
class ContactMessage(Base):
    __tablename__ = "contact_messages"

    message_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)  # Optional if user is logged in
    phone_number = Column(String(15), nullable=False)
    message = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="contact_messages")