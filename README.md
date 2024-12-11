Certainly! Below is the **README.md** file for **Task 1: CRUD Operations API** based on the user and order data, similar to how we structured the LLM Task 2 readme:
---

### **image for CRUD OPERATIONS:
![CRUD](https://github.com/user-attachments/assets/e488ead2-ab18-47ab-bc9a-26b29424592e)


---

---

# **CRUD Operations API - Task 1**

## **Project Overview**

This project implements a **CRUD (Create, Read, Update, Delete) API** for managing **Users** and **Orders**. The API is built using **FastAPI** and interacts with a PostgreSQL database. The primary goal of this API is to manage user and order data, enabling users to perform CRUD operations on both entities.

### **Technologies Used:**

- **FastAPI** - A modern, fast web framework for building APIs with Python.
- **SQLAlchemy** - A Python ORM (Object Relational Mapper) to interact with the PostgreSQL database.
- **PostgreSQL** - Relational database used to store user and order data.
- **Pydantic** - Data validation library for defining request and response models.
- **Uvicorn** - ASGI server to run FastAPI.
- **Docker** (Optional) - For containerizing the app and database for development and production environments.

---

## **Database Schema**

Two tables have been defined in the PostgreSQL database:

### **Users Table:**

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### **Orders Table:**

```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id),
  product_name VARCHAR(255) NOT NULL,
  quantity INT CHECK (quantity > 0),
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## **API Endpoints**

The API provides the following CRUD operations for both **users** and **orders**:

### **Users Endpoints:**

- `POST /users/` - Create a new user.
- `GET /users/{user_id}` - Fetch a user's details by ID.
- `PUT /users/{user_id}` - Update a user's information by ID.
- `DELETE /users/{user_id}` - Delete a user by ID.

### **Orders Endpoints:**

- `POST /orders/` - Create a new order.
- `GET /orders/{order_id}` - Fetch an order's details by ID.
- `PUT /orders/{order_id}` - Update an order's details by ID.
- `DELETE /orders/{order_id}` - Delete an order by ID.

---

## **Installation and Setup**

### **1. Clone the Repository:**

```bash
git clone https://github.com/JANNATHA-MANISH/CRUD-OPERATIONS-API.git
cd CRUD-OPERATIONS-API
```

### **2. Set up Virtual Environment:**

#### If you are using `venv`:
```bash
python -m venv venv
```

#### Activate the virtual environment:

- **Windows:**
```bash
.\venv\Scripts\activate
```

- **Linux/macOS:**
```bash
source venv/bin/activate
```

### **3. Install Dependencies:**

Install all required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### **4. Database Configuration:**

Ensure you have a PostgreSQL database running and set the **DATABASE_URL** in the `.env` file:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/mydatabase
```

Make sure that your PostgreSQL service is running and accessible.

### **5. Running the Application:**

#### Start the server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The app will be available at `http://127.0.0.1:8000`.

---

## **API Testing**

Once the server is running, you can access the **Swagger UI** to interact with the API:

- **Swagger UI URL**: `http://127.0.0.1:8000/docs`

You can use this interface to test the API endpoints and perform CRUD operations on **users** and **orders**.

---

## **Error Handling**

The API includes error handling for the following scenarios:

- **Invalid input** (e.g., missing required fields).
- **Database errors** (e.g., unique constraint violations for email).
- **Not found errors** (e.g., when a user or order does not exist).

---

## **Example Usage**

### **Create User:**

Send a `POST` request to `/users/` with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john@example.com"
}
```

### **Create Order:**

Send a `POST` request to `/orders/` with the following JSON body:

```json
{
  "user_id": 1,
  "product_name": "Laptop",
  "quantity": 2
}
```

### **Get User by ID:**

Send a `GET` request to `/users/1` to retrieve the user with ID 1.

---

## **Security**

- SSL/TLS should be enabled to ensure secure communication over HTTPS.
- The `.env` file is used to store sensitive information like database credentials. Ensure it is **never committed to version control**.

---

## **Testing**

Unit tests for each endpoint are located in the `app/tests` directory. You can run the tests using the following command:

```bash
pytest
```

---

## **Docker Setup** (Optional)

To run the API and PostgreSQL database in Docker containers, use the following steps:

### **1. Build Docker Containers:**

```bash
docker-compose up --build
```

### **2. Access the Application:**

Once the containers are up, the application will be available at `http://localhost:8000`.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



This **README** provides the necessary details to run and test the **CRUD Operations API** for managing users and orders, and integrates with PostgreSQL.
