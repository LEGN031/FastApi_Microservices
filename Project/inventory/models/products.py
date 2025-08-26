from redis_om import HashModel
from db import db

class Product(HashModel):
    name: str
    price: float
    quantity: int
    
    class Meta:
        database = db.redis