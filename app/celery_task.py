import time
from app.main import celery, app

""" Functions to show how works background tasks """
@celery.task
def call_background_task(message):
    time.sleep(10)
    print(f"Background Task called!")
    print(message)

@app.get("/test_1")
async def hello_world(message: str):
    call_background_task.delay(message)
    return {'message': 'Hello World!'}