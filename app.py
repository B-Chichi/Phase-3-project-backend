from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from models import get_db,Product
from schemas import ProductSchema
from sqlalchemy.orm import Session

app=FastAPI()

app.add_middleware(CORSMiddleware,allow_origins=["*"])

@app.get("/products")
def get_products(session:Session=Depends(get_db)):
    products=session.query(Product).all()
    print("Product created succesfully")
    return products

@app.post("/products")
def add_product(product=ProductSchema, session: Session = Depends(get_db)):
    return {"message":"Product created successfully"}

@app.get("/products/{id}")
def get_product(id):
    print ("Product",id)
    return {}

@app.patch("/products/{id}")
def update_product(id):
    print("Product updated successfully")
