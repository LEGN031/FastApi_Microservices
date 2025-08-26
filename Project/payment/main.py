from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from starlette.requests import Request
import requests
from models.Payments import Order

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods = ['*'],
    allow_headers = ['*']
    )

@app.post('/orders')
async def create(request : Request): #id, quantity
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

    orderCompleted(order)
    return order

def orderCompleted(order : Order):
    order.status = 'paid'
    order.save()