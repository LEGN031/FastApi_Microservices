from db.db import redis
from models.products import Product
import time


key = 'order_completed'
group = 'inventory_group'

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
                try:
                    product = Product.get(obj['productID'])
                    print (product)
                    product.quantity -= int(obj['quantity'])
                    product.save()
                except:
                    redis.xadd('refund_order', obj, '*')
    except Exception as e:
        print(str(e))
    time.sleep(1)