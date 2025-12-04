from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.scraper import HunnitScraper
from app.models.product import Product
from typing import List
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from app.services.rag import RAGService

def scrape_and_store(db: Session):
    scraper = HunnitScraper()
    rag_service = RAGService()
    products_data = scraper.run()
    
    count = 0
    for p_data in products_data:
        # Generate embedding
        text_to_embed = f"{p_data.get('title', '')} {p_data.get('description', '')} {p_data.get('features', '')}"
        embedding = rag_service.generate_embedding(text_to_embed)
        p_data["embedding"] = embedding

        # Check if product exists
        existing_product = db.query(Product).filter(Product.product_url == p_data["product_url"]).first()
        
        if existing_product:
            # Update fields
            for key, value in p_data.items():
                if key != "id": # Don't update ID
                    setattr(existing_product, key, value)
        else:
            # Create new
            # Remove 'id' from p_data if it exists to let DB handle PK
            if "id" in p_data:
                del p_data["id"]
            new_product = Product(**p_data)
            db.add(new_product)
            count += 1
    
    try:
        db.commit()
        logger.info(f"Scraping completed. Added {count} new products.")
    except Exception as e:
        db.rollback()
        logger.error(f"Error saving products: {e}")

@router.post("/run")
def run_scrape(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Trigger a background scraping task.
    """
    background_tasks.add_task(scrape_and_store, db)
    return {"message": "Scraping started in background"}
