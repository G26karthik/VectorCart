# Loom Video Script: VectorCart Demo

**Time Limit:** 2-3 Minutes
**Goal:** Showcase functionality, architecture, and product thinking.

---

## 1. Introduction (0:00 - 0:30)
*   **Visual:** Start with your face or the VectorCart Home Page.
*   **Script:**
    > "Hi, I'm Karthik. This is VectorCart, an AI-powered product discovery assistant I built for the Neusearch AI assignment.
    > The goal was to move beyond simple keyword search and allow users to find products using natural, abstract language—like asking for 'gym wear that works for meetings'.
    > I built this using a modern stack: FastAPI backend, React frontend, PostgreSQL with PgVector, and Google Gemini for the AI intelligence."

## 2. Live Demo - The "Wow" Factor (0:30 - 1:30)
*   **Visual:** Navigate to the **Chat** page on your deployed Vercel link.
*   **Action:** Type the query: *"Looking for something I can wear in the gym and also in meetings."*
*   **Script:**
    > "Let's see it in action. A typical search bar fails here, but VectorCart understands intent.
    > I'll ask: 'Looking for something I can wear in the gym and also in meetings.'
    > [Wait for response]
    > You can see it retrieved relevant products—like this Polo Neck Sweatshirt—and the AI explains *why* it fits both contexts: it's sporty but has a collar for a professional look.
    > This is powered by a RAG pipeline using Gemini Embeddings and PgVector."

## 3. Data & Scraping (1:30 - 2:00)
*   **Visual:** Briefly show the **Home Page** with the grid of products, then switch to the **Swagger UI (`/docs`)** or your **Code Editor (`scraper.py`)**.
*   **Script:**
    > "To populate this, I built a custom scraper for **Hunnit.com**.
    > Instead of parsing fragile HTML, I reverse-engineered their Shopify API to fetch clean JSON data directly.
    > This ensures reliable data ingestion—capturing titles, prices, and descriptions which are then vectorized for search."

## 4. Architecture & Code (2:00 - 2:30)
*   **Visual:** Show the **Mermaid Diagram** in your README or the `docker-compose.yaml` file.
*   **Script:**
    > "The system is fully containerized with Docker.
    > The backend uses FastAPI for high-performance async handling.
    > For the database, I chose PostgreSQL with the PgVector extension. This keeps the architecture simple—relational data and vector embeddings live in the same place, reducing complexity."

## 5. Conclusion (2:30 - 3:00)
*   **Visual:** Back to the Frontend or your GitHub Repo.
*   **Script:**
    > "In summary, VectorCart demonstrates an end-to-end AI application: from data ingestion to semantic retrieval and generation.
    > It's live, deployed on Render and Vercel, and ready to use.
    > Thanks for watching!"

---

**Tips for Recording:**
*   **Audio:** Ensure your microphone is clear.
*   **Pacing:** Speak clearly and not too fast.
*   **Mouse:** Move your mouse smoothly; avoid erratic movements.
*   **Preparation:** Have the tabs (App, Swagger, GitHub) open before you start.
