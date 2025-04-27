from fastapi import FastAPI, Depends
from routes.auth import router as auth_router
from routes.fetchOrders import router as orders 
from database import Base, engine
from fastapi.security import OAuth2PasswordBearer

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.get("/protected-route")
def protected_route(token: str = Depends(oauth2_scheme)):
    return {"message": "You are authorized!"}

# Include Auth Routes
app.include_router(auth_router, prefix="", tags=["Authentication"])
app.include_router(orders)
