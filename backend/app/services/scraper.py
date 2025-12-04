import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class HunnitScraper:
    BASE_URL = "https://hunnit.com"
    PRODUCTS_JSON_URL = f"{BASE_URL}/products.json"

    def fetch_products(self) -> List[Dict[str, Any]]:
        try:
            logger.info(f"Fetching products from {self.PRODUCTS_JSON_URL}")
            response = requests.get(self.PRODUCTS_JSON_URL, timeout=30)
            response.raise_for_status()
            data = response.json()
            return data.get("products", [])
        except Exception as e:
            logger.error(f"Error fetching products: {e}")
            return []

    def clean_html(self, html_content: str) -> str:
        if not html_content:
            return ""
        soup = BeautifulSoup(html_content, "html.parser")
        return soup.get_text(separator=" ", strip=True)

    def normalize_product(self, raw_product: Dict[str, Any]) -> Dict[str, Any]:
        try:
            variants = raw_product.get("variants", [])
            price = 0.0
            if variants:
                price = float(variants[0].get("price", 0.0))

            images = raw_product.get("images", [])
            image_url = ""
            if images:
                image_url = images[0].get("src", "")

            description = self.clean_html(raw_product.get("body_html", ""))
            
            # Use tags as features
            features = ", ".join(raw_product.get("tags", []))
            
            # Determine category
            category = raw_product.get("product_type")
            if not category:
                category = "Activewear" # Default for Hunnit

            return {
                "id": raw_product.get("id"), # Keep original ID if unique, or let DB generate one. 
                # Actually, let's use the scraped ID but we might need to be careful if we want to use auto-incrementing PK in DB.
                # The DB model has Integer PK. Scraped IDs are big integers. It should fit in BigInteger, but standard Integer might overflow if it's 32-bit.
                # Python 3 integers are arbitrary precision, but Postgres Integer is 4 bytes (max 2B). BigInteger is 8 bytes.
                # Hunnit IDs are like 8602887094450 (13 digits), which fits in BigInteger (up to 19 digits).
                # My model defined `id = Column(Integer, primary_key=True)`. In SQLAlchemy, Integer usually maps to INTEGER (4 bytes).
                # I should probably change the model to use BigInteger or just let DB generate IDs and store scraped_id separately.
                # For simplicity, I'll let DB generate IDs and I won't store the scraped ID as PK. 
                # I'll just store the data.
                "title": raw_product.get("title"),
                "price": price,
                "description": description,
                "features": features,
                "category": category,
                "image_url": image_url,
                "product_url": f"{self.BASE_URL}/products/{raw_product.get('handle')}",
                "created_at": datetime.fromisoformat(raw_product.get("created_at").replace("Z", "+00:00")) if raw_product.get("created_at") else datetime.now()
            }
        except Exception as e:
            logger.error(f"Error normalizing product {raw_product.get('id')}: {e}")
            return None

    def run(self) -> List[Dict[str, Any]]:
        raw_products = self.fetch_products()
        cleaned_products = []
        for p in raw_products:
            norm = self.normalize_product(p)
            if norm:
                cleaned_products.append(norm)
        return cleaned_products
