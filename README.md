# FastAPI Online Shop 🛒

**Online Shop API** is a high-performance, asynchronous e-commerce ecosystem built with **FastAPI**. It provides a robust backend for managing product catalogs, user roles, shopping carts, and secure order processing.

---

## 🏗 Architecture & Data Flow

The project follows a modular design with a clear separation of concerns:

1. **API Layer:** FastAPI handles incoming requests with high throughput using `asyncio`.
2. **Auth System:** Multi-level access control (Buyer/Seller/Admin) via JWT (Access & Refresh tokens).
3. **Data Persistence:** Asynchronous interaction with PostgreSQL via `SQLAlchemy 2.0`.
4. **Business Logic:** Secure order snapshots that preserve product prices at the moment of purchase.
5. **Validation:** Strict data integrity using `Pydantic v2` models.

---

## 🛠 Tech Stack

* **Core:** Python 3.13, Asyncio
* **Backend:** FastAPI (Uvicorn)
* **Database:** PostgreSQL + `asyncpg` (Asynchronous driver)
* **ORM & Migrations:** SQLAlchemy 2.0, Alembic
* **Security:** JWT (Access/Refresh), Passlib (bcrypt)
* **Data Schemas:** Pydantic v2

---

## 📡 API Endpoints

### 📁 Categories
* `GET /categories/` — Get All Categories.
* `POST /categories/` — Create Category.
* `PUT /categories/{category_id}` — Update Category.
* `DELETE /categories/{category_id}` — Delete Category.

### 📦 Products
* `GET /products/` — Get All Products.
* `POST /products/` — Create Product (🔒).
* `GET /products/category/{category_id}` — Get Products By Category.
* `GET /products/{product_id}` — Get Product details.
* `PUT /products/{product_id}` — Update Product (🔒).
* `DELETE /products/{product_id}` — Delete Product (🔒).
* `GET /products/{product_id}/reviews/` — Get Product Reviews.

### 🔐 Users & Auth
* `POST /users/` — Create User (Register).
* `POST /users/token` — Login (Obtain tokens).
* `POST /users/refresh-token` — Refresh Token.

### 🛒 Cart
* `GET /cart/` — Get Cart (🔒).
* `DELETE /cart/` — Clear Cart (🔒).
* `POST /cart/items` — Add Item To Cart (🔒).
* `PUT /cart/items/{product_id}` — Update Cart Item (🔒).
* `DELETE /cart/items/{product_id}` — Remove Item From Cart (🔒).

### 💳 Orders
* `POST /orders/checkout` — Checkout Order (🔒).
* `GET /orders/` — List Orders (🔒).
* `GET /orders/{order_id}` — Get Order details (🔒).

### ⭐ Reviews
* `GET /reviews/` — Get Reviews.
* `POST /reviews/` — Create Review (🔒).
* `DELETE /reviews/{review_id}` — Delete Review (🔒).
  
---
## ⚙️ Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/youmiiii1/FastAPI-Shop.git](https://github.com/youmiiii1/FastAPI-Shop.git)
   cd FastAPI-Shop
    ```
2. **Create & Activate Virtual Environment:**
   ```bash
   python -m venv venv
    # Windows:
    venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Database Migrations:**
    ```bash
    # Make sure your DATABASE_URL is set in .env
    alembic upgrade head
    ```
5. **Run the Application:**
   ```bash
   uvicorn app.main:app --reload
   ```
## 📖 Documentation
Once the server is running, explore the interactive documentation:
* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
