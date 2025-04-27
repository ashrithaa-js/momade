from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from crud import get_sorted_orders, create_order
from schemas import OrderCreate, OrderResponse
from .auth import get_current_admin 
from .dependencies import get_current_user


router = APIRouter(prefix="/orders", tags=["Orders"])
@router.get("/list", response_model=list[OrderResponse])
def fetch_orders(db: Session = Depends(get_db), admin: dict = Depends(get_current_admin)):
    orders = get_sorted_orders(db)
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found")
    return orders

@router.post("/place", response_model=OrderResponse)
def place_order(
    order_data: OrderCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)  # Ensures user is authenticated
):
    """
    Place an order (only for logged-in customers).
    """
    if current_user["role"] != "customer":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only customers can place orders")

    order = create_order(db, current_user["user_id"], order_data)
    if isinstance(order, dict) and "error" in order:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=order["error"])

    return order
