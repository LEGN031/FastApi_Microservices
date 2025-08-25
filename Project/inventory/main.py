from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel

app = FastAPI()

redis = get_redis_connection(
    host = "redis-11517.c61.us-east-1-3.ec2.redns.redis-cloud.com",
    port = 11517,
    password = "1H1j4xZcC6nxiaR4rLzIX2n71KxYLEd1",
    decode_responses = True
)




@app.get("/products")
def all():
    return []

