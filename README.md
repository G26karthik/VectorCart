# VectorCart - AI-Powered Product Discovery Assistant

**VectorCart** is a full-stack AI e-commerce assistant that I built to solve the problem of finding the right products using natural language. It scrapes product data, understands abstract queries (like "gym and office wear"), and provides personalized recommendations using RAG (Retrieval Augmented Generation).

## 🔗 Live Demo

*   **Frontend (Store):** [https://vector-cart-rho.vercel.app/](https://vector-cart-rho.vercel.app/)
*   **Backend API:** [https://vectorcart-api.onrender.com/docs](https://vectorcart-api.onrender.com/docs)

## 🚀 Key Features

*   **Smart Search:** You don't need to match keywords exactly. Ask for "something for yoga" or "outfit for a date", and it understands.
*   **Real Data:** I built a custom scraper that fetches real-time product data from **Hunnit.com**.
*   **AI Recommendations:** Uses **Google Gemini** to explain *why* a product is a good match for you.
*   **Modern Stack:** Built with performance in mind using FastAPI, React, and PgVector.

## 🛠️ Tech Stack

*   **Backend:** Python, FastAPI, SQLAlchemy
*   **Database:** PostgreSQL + PgVector (for storing AI embeddings)
*   **AI/LLM:** Google Gemini API (`models/text-embedding-004` & `gemini-flash-latest`)
*   **Frontend:** React, TypeScript, Vite, TailwindCSS
*   **Infrastructure:** Docker, Render (Backend), Vercel (Frontend)

## 🏗️ How It Works

1.  **Scraping:** The system fetches product details (title, price, description) from Hunnit.com.
2.  **Embedding:** Each product is converted into a vector embedding using Gemini's text embedding model.
3.  **Retrieval:** When you ask a question, your query is also converted into a vector. The system then finds the products that are mathematically closest to your query in the vector space.
4.  **Generation:** The top results are sent to the Gemini LLM, which generates a helpful, human-like response recommending the best options.

## 🏃‍♂️ Running Locally

If you want to run this on your own machine:

1.  **Clone the repo:**
    ```bash
    git clone https://github.com/G26karthik/VectorCart.git
    cd VectorCart
    ```

2.  **Set up Environment Variables:**
    Create a `.env` file with your credentials:
    ```env
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=password
    POSTGRES_DB=product_discovery
    GEMINI_API_KEY=your_api_key_here
    ```

3.  **Run with Docker:**
    ```bash
    docker-compose up -d --build
    ```

4.  **Access the App:**
    Open [http://localhost:3000](http://localhost:3000) in your browser.

## 🌟 Future Improvements

If I had more time, here's what I'd add next:
1.  **Hybrid Search:** Combine keyword search with vector search to handle specific product names better.
2.  **Chat History:** Save conversations so you can ask follow-up questions.
3.  **Image Search:** Allow users to upload a photo to find similar products.

---
*Built by Karthik*
