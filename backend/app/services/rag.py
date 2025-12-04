import google.generativeai as genai
from app.core.config import settings
from typing import List
import logging

logger = logging.getLogger(__name__)

# Configure Gemini
genai.configure(api_key=settings.GEMINI_API_KEY)

class RAGService:
    def __init__(self):
        self.model_name = "models/text-embedding-004"

    def generate_embedding(self, text: str) -> List[float]:
        try:
            # Clean text
            text = text.replace("\n", " ")
            result = genai.embed_content(
                model=self.model_name,
                content=text,
                task_type="retrieval_document",
                title="Product Embedding"
            )
            return result['embedding']
        except Exception as e:
            logger.error(f"Error generating embedding: {e}")
            return []

    def generate_query_embedding(self, text: str) -> List[float]:
        try:
            text = text.replace("\n", " ")
            result = genai.embed_content(
                model=self.model_name,
                content=text,
                task_type="retrieval_query"
            )
            return result['embedding']
        except Exception as e:
            logger.error(f"Error generating query embedding: {e}")
            return []

    def generate_response(self, query: str, context: str) -> str:
        try:
            model = genai.GenerativeModel('gemini-flash-latest')
            prompt = f"""
            You are an AI product discovery assistant for Hunnit (activewear brand).
            User Query: {query}
            
            Here are some relevant products found in our catalog:
            {context}
            
            Your goal is to help the user find the best product.
            1. Analyze the user's query and the provided products.
            2. If the query is vague (e.g., "something for gym"), ask 1-2 short clarifying questions to narrow it down (e.g., "Do you prefer leggings or shorts?").
            3. If the query is specific or you have good matches, recommend the best products from the context.
            4. Explain WHY you chose them (mention features like fabric, fit, etc.).
            5. If the context doesn't contain relevant products, politely say so.
            6. Do NOT invent products. Only use the provided context.
            
            Keep your response helpful, friendly, and concise.
            """
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return "I'm sorry, I encountered an error while processing your request."
