# VectorCart - AI-Powered Product Discovery Assistant

**VectorCart** is a full-stack AI e-commerce assistant that scrapes product data, stores it with vector embeddings, and provides intelligent product recommendations using RAG (Retrieval Augmented Generation).

## 🚀 Features

*   **Automated Scraping:** Fetches and normalizes product data from **Hunnit.com**.
*   **Vector Search:** Uses **PgVector** and **Gemini Embeddings** for semantic search.
*   **AI Chatbot:** **Gemini-powered** assistant that understands abstract queries (e.g., "gym and office wear").
*   **Modern Stack:** FastAPI, PostgreSQL, React, Vite, TailwindCSS, Docker.

## 🛠️ Tech Stack

*   **Backend:** Python, FastAPI, SQLAlchemy, Alembic, BeautifulSoup
*   **Database:** PostgreSQL + PgVector
*   **AI/LLM:** Google Gemini API (`models/text-embedding-004`, `gemini-flash-latest`)
*   **Frontend:** React, TypeScript, Vite, TailwindCSS
*   **Infrastructure:** Docker, Docker Compose

## 🏃‍♂️ How to Run Locally

1.  **Prerequisites:**
    *   Docker Desktop installed and running.
    *   Google Gemini API Key.

2.  **Setup Environment:**
    *   Create a `.env` file in the root directory:
        ```env
        POSTGRES_USER=postgres
        POSTGRES_PASSWORD=password
        POSTGRES_SERVER=db
        POSTGRES_PORT=5432
        POSTGRES_DB=product_discovery
        GEMINI_API_KEY=your_api_key_here
        ```

3.  **Start Application:**
    ```bash
    docker-compose up -d --build
    ```

4.  **Trigger Scraping:**
    *   Once running, trigger the initial data scrape:
        ```bash
        curl -X POST http://localhost:8000/api/v1/scrape/run
        ```

5.  **Access the App:**
    *   **Frontend:** [http://localhost:3000](http://localhost:3000)
    *   **Backend API:** [http://localhost:8000/docs](http://localhost:8000/docs)

## 🏗️ Architecture & Decisions

*   **FastAPI:** Chosen for its speed and native support for async operations, crucial for handling concurrent scraping and AI requests.
*   **PgVector:** Integrated directly into PostgreSQL to keep the stack simple (single database for relational and vector data) and reduce infrastructure complexity.
*   **Gemini API:** Selected for its cost-effectiveness and strong performance in both embedding and generation tasks.
*   **Docker:** Ensures consistent environments across development and deployment.

## 🕷️ Scraping Approach

*   **Target:** Hunnit.com
*   **Method:** Utilizes `requests` and `BeautifulSoup` to fetch the `products.json` endpoint provided by Shopify-based stores. This ensures reliable, structured data extraction without parsing complex HTML DOMs.
*   **Data Cleaning:** Normalizes prices, descriptions (stripping HTML tags), and categories to ensure high-quality input for the RAG pipeline.

## 🧠 RAG Pipeline Design

1.  **Ingestion:** Scraped products are converted into text chunks (Title + Description + Features).
2.  **Embedding:** Text chunks are embedded using `models/text-embedding-004`.
3.  **Storage:** Embeddings are stored in the `products` table using the `vector` column type.
4.  **Retrieval:** User queries are embedded and compared against stored vectors using Cosine Similarity (`<=>` operator).
5.  **Generation:** Top 5 relevant products are passed as context to `gemini-flash-latest` to generate a personalized, explained recommendation.

## ⚠️ Challenges & Trade-offs

*   **Model Deprecation:** Initially used `gemini-pro`, which returned 404 errors. Switched to `gemini-flash-latest` for reliable access.
*   **Scraping Reliability:** Direct HTML scraping is fragile. Switched to consuming the JSON endpoint for stability.
*   **Context Window:** Limited to top 5 products to balance context window usage and relevance.

## 🌟 Bonus: Future Improvements

If I had more time, I would implement:
1.  **Hybrid Search:** Combine keyword search (BM25) with vector search for better precision on specific product names.
2.  **Chat History:** Store conversation history in Redis or Postgres to allow multi-turn conversations.
3.  **Image Search:** Implement multi-modal embeddings to allow users to search by uploading images.
4.  **Live Scraping:** Implement a Celery task queue to schedule periodic scraping for real-time inventory updates.

## 📦 Deployment Guide

### Backend (Render/Railway)
1.  Push code to GitHub.
2.  Connect repository to Render/Railway.
3.  Set environment variables (`GEMINI_API_KEY`, `DATABASE_URL`).
4.  Update `start` command to: `sh entrypoint.sh`.

### Frontend (Vercel)
1.  Push code to GitHub.
2.  Import project in Vercel.
3.  Set `VITE_API_URL` to your deployed backend URL.
4.  Deploy.
