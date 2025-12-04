import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not found in environment.")
    exit(1)

genai.configure(api_key=api_key)

def test_embedding():
    print("Testing Embedding (models/embedding-001)...")
    try:
        model = "models/embedding-001"
        result = genai.embed_content(
            model=model,
            content="Hello world",
            task_type="retrieval_document"
        )
        print("Embedding Success!")
        return True
    except Exception as e:
        print(f"Embedding Failed: {e}")
        return False

def test_generation():
    print("\nTesting Generation (gemini-pro)...")
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Hello, are you working?")
        print(f"Generation Success! Response: {response.text}")
        return True
    except Exception as e:
        print(f"Generation Failed: {e}")
        return False

if __name__ == "__main__":
    embed_ok = test_embedding()
    gen_ok = test_generation()
    
    if not embed_ok or not gen_ok:
        print("\nTrying alternative models...")
        # Try newer models
        try:
            print("Testing Embedding (models/text-embedding-004)...")
            genai.embed_content(model="models/text-embedding-004", content="test")
            print("New Embedding Model Success!")
        except Exception as e:
            print(f"New Embedding Model Failed: {e}")

        try:
            print("Testing Generation (gemini-1.5-flash)...")
            model = genai.GenerativeModel('gemini-1.5-flash')
            model.generate_content("test")
            print("New Generation Model Success!")
        except Exception as e:
            print(f"New Generation Model Failed: {e}")
