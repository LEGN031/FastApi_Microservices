from redis_om import get_redis_connection
from config.env import a

redis = get_redis_connection( 
    host=a.REDIS_HOST, 
    port=a.REDIS_PORT, 
    password=a.REDIS_PASSWORD, 
    decode_responses=True )