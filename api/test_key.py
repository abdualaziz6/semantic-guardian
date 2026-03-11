import os
from dotenv import load_dotenv
from google import genai

# Load your .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: GEMINI_API_KEY not found in your .env file!")
else:
    print(f"✅ Key detected: {api_key[:8]}...")
    
    # Initialize the NEW 2026 Client
    client = genai.Client(api_key=api_key)
    
    try:
        # We use Gemini 3 Flash for the best hackathon speed/cost balance
        response = client.models.generate_content(
            model="gemini-3-flash-preview", 
            contents="Say 'System Online'"
        )
        print(f"🚀 Gemini says: {response.text}")
    except Exception as e:
        print(f"❌ Connection failed: {e}")