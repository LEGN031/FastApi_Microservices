from database.db import redis
from models.Payments import Order
import time


key = 'refund_order'
group = 'payment_group'

try:
    redis.xgroup_create(key, group)
except:
    print('Group already exists')


while True:
    try:
        results = redis.xreadgroup(group, key, {key: '>'}, None)

        if results is not []:
            print(results)
            for result in results:
                obj=result[1][0][1]
                order = Order.get(obj['pk'])
                order.status = 'refunded'
                order.save()
    except Exception as e:
        print(str(e))
    time.sleep(1)