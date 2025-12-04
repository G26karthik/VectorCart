from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.product import Product
from app.services.rag import RAGService
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ChatRequest(BaseModel):
    query: str

class ProductRecommendation(BaseModel):
    id: int
    title: str
    price: float
    image_url: Optional[str] = None
    product_url: Optional[str] = None

class ChatResponse(BaseModel):
    message: str
    recommended_products: List[ProductRecommendation]

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    rag_service = RAGService()
    
    # 1. Generate query embedding
    query_embedding = rag_service.generate_query_embedding(request.query)
    
    if not query_embedding:
        raise HTTPException(status_code=500, detail="Failed to generate query embedding")
    
    # 2. Retrieve top-k products
    # Using cosine distance (operator <=> in pgvector, but here we use cosine_distance method)
    # Note: pgvector-python's cosine_distance returns distance (lower is better)
    top_products = db.query(Product).order_by(
        Product.embedding.cosine_distance(query_embedding)
    ).limit(5).all()
    
    # 3. Construct context
    context = ""
    recommendations = []
    for p in top_products:
        context += f"Product ID: {p.id}\nTitle: {p.title}\nPrice: {p.price}\nDescription: {p.description}\nFeatures: {p.features}\n\n"
        recommendations.append(ProductRecommendation(
            id=p.id,
            title=p.title,
            price=p.price,
            image_url=p.image_url,
            product_url=p.product_url
        ))
    
    # 4. Generate LLM response
    llm_response = rag_service.generate_response(request.query, context)
    
    return ChatResponse(
        message=llm_response,
        recommended_products=recommendations
    )
