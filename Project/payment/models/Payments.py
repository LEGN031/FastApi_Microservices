from redis_om import HashModel

from database import db

class Order(HashModel):
    productID: str
    price: float
    fee: float
    total: float
    quantity : int
    status: str
    
    class Meta:
        database = db.redis

    