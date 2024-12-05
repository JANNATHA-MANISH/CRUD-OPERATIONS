from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from . import crud, schemas, dependencies  # Import from dependencies.py

app = FastAPI()

# User Endpoints
@app.post("/users", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db_session)):
    try:
        return crud.create_user(db=db, user=user)
    except HTTPException as e:
        raise e  # Propagate custom HTTPException if raised
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.get("/users/{user_id}", response_model=schemas.User)
async def get_user(user_id: int, db: Session = Depends(dependencies.get_db_session)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=schemas.User)
async def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(dependencies.get_db_session)):
    db_user = crud.update_user(db=db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(dependencies.get_db_session)):
    db_user = crud.get_user(db=db, user_id=user_id)  # Check if the user exists before attempting to delete
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    crud.delete_user(db=db, user_id=user_id)
    return JSONResponse(content={"message": "User deleted successfully"}, status_code=200)

# Order Endpoints
@app.post("/orders", response_model=schemas.Order)
async def create_order(order: schemas.OrderCreate, db: Session = Depends(dependencies.get_db_session)):
    # Check if the user exists before creating an order
    db_user = crud.get_user(db=db, user_id=order.user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail=f"User with ID {order.user_id} not found")

    return crud.create_order(db=db, order=order)

@app.get("/orders/{order_id}", response_model=schemas.Order)
async def get_order(order_id: int, db: Session = Depends(dependencies.get_db_session)):
    db_order = crud.get_order(db=db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@app.put("/orders/{order_id}", response_model=schemas.Order)
async def update_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(dependencies.get_db_session)):
    db_order = crud.update_order(db=db, order_id=order_id, order=order)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@app.delete("/orders/{order_id}")
async def delete_order(order_id: int, db: Session = Depends(dependencies.get_db_session)):
    db_order = crud.get_order(db=db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    crud.delete_order(db=db, order_id=order_id)
    return JSONResponse(content={"message": "Order deleted successfully"}, status_code=200)
