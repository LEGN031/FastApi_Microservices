from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks
from fastapi import HTTPException
from starlette.requests import Request
import requests, time
from models.Payments import Order
from database.db import redis

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods = ['*'],
    allow_headers = ['*']
    )

@app.post('/orders')
async def create(request : Request, background_task: BackgroundTasks): #id, quantity
    body = await request.json()
    req = requests.get('http://inventory:8000/products/%s' % body['id'])
    product = req.json()

    order = Order(
        productID = body['id'],
        price = product['price'],
        fee = product['price'] * 0.2,
        total = product['price'] * 1.2,
        quantity=body['quantity'],
        status = 'pending'
    )
    order.save()

    background_task.add_task(orderCompleted, order)
    return order

def orderCompleted(order : Order):
    time.sleep(5)
    order.status = 'paid'
    order.save()
    redis.xadd('order_completed', order.model_dump(), '*')

@app.get('/orders')
async def index():
    if len(list(Order.all_pks())) > 0:
        return [Order.get(pk) for pk in list(Order.all_pks())]
    raise HTTPException(status_code=404, detail="No orders found")

@app.get('/orders/{pk}')
async def get(pk: str):
    order = Order.get(pk)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order