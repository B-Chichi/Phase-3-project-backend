from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import get_db, Product, Supplier, Order
from schemas import ProductSchema, SupplierSchema, OrderSchema
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


@app.get("/products")
def get_products(session: Session = Depends(get_db)):
    return session.query(Product).all()


@app.post("/products")
def add_product(product: ProductSchema, session: Session = Depends(get_db)):
    new_product = Product(**product.model_dump())
    session.add(new_product)
    session.commit()
    return {"message": "Product created successfully", "Product": product}


@app.get("/products/{id}")
def get_product(id: int, session: Session = Depends(get_db)):
    product = session.query(Product).filter_by(id=id).first()
    if not product:
        return {"error": "Product not found"}
    return product


@app.patch("/products/{id}")
def update_product(id: int, stock: int, session: Session = Depends(get_db)):
    product = session.query(Product).filter_by(id=id).first()
    if not product:
        return {"error": "Product not found"}
    product.stock = stock
    session.commit()
    return {"message": "Product stock updated"}


@app.delete("/products/{id}")
def delete_product(id: int, session: Session = Depends(get_db)):
    product = session.query(Product).filter_by(id=id).first()
    if not product:
        return {"error": "Product not found"}
    session.delete(product)
    session.commit()
    return {"message": "Product deleted successfully"}


@app.post("/suppliers/")
def add_supplier(supplier: SupplierSchema, session: Session = Depends(get_db)):
    new_supplier = Supplier(**supplier.model_dump())
    session.add(new_supplier)
    session.commit()
    return {"message": "Supplier added successfully"}


@app.get("/suppliers/")
def get_suppliers(session: Session = Depends(get_db)):
    return session.query(Supplier).all()


@app.post("/orders/")
def create_order(order: OrderSchema, session: Session = Depends(get_db)):
    product = session.query(Product).filter_by(id=order.product_id).first()
    if not product or product.stock < order.quantity:
        return {"error": "Insufficient stock or product unavailable"}
    product.stock -= order.quantity
    session.commit()
    new_order = Order(
        product_id=order.product_id,
        quantity=order.quantity,
        customer_name=order.customer_name,
    )
    session.add(new_order)
    session.commit()
    return {"message": "Order placed successfully"}


@app.get("/products/low-stock")
def get_low_stock_products(session: Session = Depends(get_db)):
    return session.query(Product).filter(Product.stock <= Product.min_stock).all()
