from redis_om import HashModel
import main

class product(HashModel):
    name: str
    prices: float
    quantity: int
    
    class Meta:
        database = main.redis