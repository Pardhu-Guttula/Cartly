from fastapi import APIRouter, Query, HTTPException
from sqlalchemy.orm import Session
from backend.models import product, category
from backend.schemas import ProductSearchResults, Product as ProductSchema
from backend.services.database import get_db

# Epic Title: Implement Efficient Product Search Functionality

router = APIRouter()

@router.get("/search", response_model=ProductSearchResults)
def search_products(
    query: str = Query(None, title="Query string for searching products"),
    category_id: int = Query(None, title="Category ID to filter products"),
    min_price: float = Query(None, title="Minimum price to filter products"),
    max_price: float = Query(None, title="Maximum price to filter products"),
    db: Session = get_db()
):
    # Implement search functionality
    filters = []
    
    if query:
        filters.append(product.Product.name.ilike(f'%{query}%'))
    
    if category_id:
        filters.append(product.Product.category_id == category_id)
    
    if min_price is not None:
        filters.append(product.Product.price >= min_price)
    
    if max_price is not None:
        filters.append(product.Product.price <= max_price)
    
    products = db.query(product.Product).filter(*filters).all()
    
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    
    return ProductSearchResults(products=[ProductSchema.from_orm(p) for p in products])