from fastapi import FastAPI    
from fastapi.middleware.cors import CORSMiddleware 
from fastapi import HTTPException 
from models import products 

app = FastAPI()

app.add_middleware( CORSMiddleware, allow_origins=['http://localhost:3000'], 
                   allow_methods = ['*'], allow_headers = ['*'] ) 

@app.get('/products') 
def all():
    if len(list(products.Product.all_pks())) > 0: 
        return [format(pk) for pk in products.Product.all_pks()] 
    raise HTTPException(status_code=404, detail='Empty list') 
@app.get('/products/{pk}') 
def byId(pk : str): 
    if pk in products.Product.all_pks(): return format(pk) 
    raise HTTPException(status_code=404, detail='Not Found') 

def format(pk:str): 
    product = products.Product.get(pk) 
    return { 
    "id" : product.pk, 
    "name" : product.name,
    "price" : product.price, 
     "quantity" : product.quantity } 

@app.post('/products') 
def createProducts(product : products.Product): 
    return product.save()


@app.delete('/products/{pk}') 
def eliminar(pk: str): 
    if pk in products.Product.all_pks(): 
        products.Product.delete(pk)
        return {"message": "Producto deleted"} 
    raise HTTPException(status_code=404, detail='Not Found') 
