from fastapi import FastAPI
from celery import Celery
from app.routers import categories, products, users, reviews, cart, orders

# Создаём приложение FastAPI
app = FastAPI(
    title="FastAPI Интернет-магазин",
    version="0.1.0",
)

celery = Celery(
    __name__,
    broker='redis://127.0.0.1:6379/0',
    backend='redis://127.0.0.1:6379/0',
    broker_connection_retry_on_startup=True,
    include=['app.celery_task']
)

# app_v1 = FastAPI(
# title="My API v1",
# description="The first version of my API",
# )
#
# app_v2 = FastAPI(
# title="My API v2",
# description="The second version of my API",
# )
#
# @app_v1.get("/products")
# async def get_products_v1():
#     return {"message": "Products API Version 1"}
#
#
# @app_v2.get("/products")
# async def get_products_v2():
#     return {"message": "Products API Version 2"}
#
# app.mount("/v1", app_v1)
# app.mount("/v2", app_v2)

# Подключаем маршруты категорий
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(users.router)
app.include_router(reviews.router)
app.include_router(cart.router)
app.include_router(orders.router)

# Корневой эндпоинт для проверки
@app.get("/")
async def root():
    """
    Корневой маршрут, подтверждающий, что API работает.
    """
    return {"message": "Добро пожаловать в API интернет-магазина!"}
