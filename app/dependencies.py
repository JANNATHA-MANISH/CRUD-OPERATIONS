from sqlalchemy.orm import Session
from .database import SessionLocal  # Import from database.py

# Dependency to get the database session
def get_db_session():
    db = SessionLocal()  # Create a new database session
    try:
        yield db  # Yield session to be used by the route
    finally:
        db.close()  # Ensure the session is closed after the request is completed
