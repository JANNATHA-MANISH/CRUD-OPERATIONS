from fastapi.testclient import TestClient
from app.main import app  # Import the app directly
import sys
import os

# Add the root directory to sys.path so Python can find the app module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.main import app  # Import your app after modifying sys.path

client = TestClient(app)

def test_create_user():
    response = client.post("/users", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    assert response.status_code == 201  # Expect 201 Created
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["email"] == "jane.doe@example.com"

def test_get_user():
    # First, create a user
    response = client.post("/users", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    user_id = response.json()["id"]  # Get the user ID from the response

    # Now, get the created user by ID
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200  # Expect 200 OK
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["email"] == "jane.doe@example.com"
