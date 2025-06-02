from pydantic import BaseModel


class ProductSchema(BaseModel):
    name: str
    price: int
    stock: int
    category: str
 


class SupplierSchema(BaseModel):
    name: str
    contact_info: str


class OrderSchema(BaseModel):
    product_id: int
    quantity: int
    customer_name:str