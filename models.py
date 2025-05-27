from sqlalchemy.orm import DeclarativeBase,sessionmaker
from sqlalchemy import Column, Integer, Text, ForeignKey,create_engine

engine = create_engine("sqlite:///project.db",echo=True)

Session=sessionmaker(bind=engine)

def get_db():
    session=Session()
    try:
        yield session
    finally:
        session.close()


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, default=0)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    contact_info = Column(Text)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False)
    customer_name = Column(Text, nullable=False)
