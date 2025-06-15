import os
import requests

def get_quote():
    api_key = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mixtral-8x7b-32768",  # Or llama3-70b-8192
        "messages": [{"role": "user", "content": "Give me a short motivational quote."}]
    }

    response = requests.post(url, json=data, headers=headers)
    result = response.json()
    return result['choices'][0]['message']['content'].strip()
# This function fetches a motivational quote from the Groq API.
# It uses the API key stored in the environment variable GROQ_API_KEY.