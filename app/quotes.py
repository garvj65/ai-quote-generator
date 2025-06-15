import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# Force load from parent directory
load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

def get_quote():
    api_key = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",  # You mentioned using llama-3.1-8b-instant (Groq maps this internally)
        "messages": [
            {"role": "user", "content": "Give me a short motivational quote."}
        ]
    }
    print("🔐 API KEY LOADED:", os.getenv("GROQ_API_KEY"))
    if not api_key:
        return "GROQ_API_KEY environment variable is not set."
    try:
        response = requests.post(url, json=data, headers=headers)
        result = response.json()

        if response.status_code != 200:
            return f"Groq API error: {response.status_code} - {response.text}"

        if "choices" not in result:
            return f"Unexpected response format: {result}"

        return result['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"Exception occurred: {str(e)}"
