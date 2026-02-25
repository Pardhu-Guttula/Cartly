from fastapi import APIRouter, Query, HTTPException
from sqlalchemy.orm import Session
from backend.models import product, category
from backend.schemas import ProductPage, Product as ProductSchema
from backend.services.database import get_db

# Epic Title: Develop Reusable Product Browsing Components

router = APIRouter()

@router.get("/browse", response_model=ProductPage)
def browse_products(
    page: int = Query(1, title="Page number for pagination"),
    page_size: int = Query(10, title="Number of products per page"),
    db: Session = get_db()
):
    offset = (page - 1) * page_size
    products = db.query(product.Product).offset(offset).limit(page_size).all()
    
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    
    total_products = db.query(func.count(product.Product.id)).scalar()
    
    return ProductPage(
        products=[ProductSchema.from_orm(p) for p in products],
        total=total_products,
        page=page,
        page_size=page_size,
    )