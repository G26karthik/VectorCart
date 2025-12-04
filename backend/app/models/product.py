from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ARRAY
from sqlalchemy.sql import func
from pgvector.sqlalchemy import Vector
from app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    price = Column(Float)
    description = Column(Text)
    features = Column(Text)  # Stored as text, can be JSON or separated by newlines
    category = Column(String, index=True)
    image_url = Column(String)
    product_url = Column(String, unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Embedding vector (assuming 768 dimensions for Gemini embeddings, adjust if needed)
    embedding = Column(Vector(768)) 
