from fastapi import FastAPI,Depends
from models import get_db,Product

app=FastAPI()

@app.get("/products")
def get_products(session=Depends(get_db)):
    products=session.query(Product).all()
    print("Product created succesfully")
    return products

@app.post("/products")
def add_product():
    return {"message":"Product created successfully"}

@app.get("/products/{id}")
def get_product(id):
    print ("Product",id)
    return {}

@app.patch("/products/{id}")
def update_product(id):
    print("Product updated successfully")
