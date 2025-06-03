# StockPilot

StockPilot is a backend-driven inventory management system built with *FastAPI* and *SQLAlchemy*, designed to handle product storage, filtering and addition of new products.

## Features 
- *Product Listing:* Retrieve all available products with FastAPI.
- *Filtering & Sorting:* Search by name and filter by category.
- *Low Stock Indicator:* Highlights low-stock items for easy tracking.
- *Add Products:* Create new products using FastAPI endpoints.

## Technologies Used 
- *FastAPI* (Modern Python web framework)
- *SQLAlchemy* (ORM for database interactions)
- *SQLite* (Database)
- *React* (Frontend)

## Backend Setup 

### Install Dependencies
Ensure you have *Python* installed, then run:
```bash
pip install "fastapi[standard]" sqlalchemy alembic 

Open http://localhost:8000/docs to test API endpoints interactively.

API Endpoints 📝
| Method | Endpoint | Description | 
| GET | /products | Retrieve all products | 
| GET | /products/{id} | Get a specific product by ID | 
| POST | /products | Add a new product | 
| PATCH| /products/{id} | Update a product | 
| DELETE | /products/{id} | Remove a product | 


[Video link](https://drive.google.com/file/d/162W64kSMsPqCBAvnAcXjSvL1fhCg-L_k/view?usp=sharing)


MIT License © 2025 Brian
