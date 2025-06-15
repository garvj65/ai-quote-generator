import app.main as app

def test_quote():
    client = app.app.test_client()
    res = client.get('/quote')
    assert res.status_code == 200
    assert "quote" in res.json


def test_quote_content():
    client = app.app.test_client()
    res = client.get('/quote')
    assert res.status_code == 200
    assert isinstance(res.json['quote'], str)
    assert len(res.json['quote']) > 0  # Ensure the quote is not empty
def test_quote_format():
    client = app.app.test_client()
    res = client.get('/quote')
    assert res.status_code == 200
    assert isinstance(res.json, dict)
    assert 'quote' in res.json
    assert isinstance(res.json['quote'], str)  # Ensure the quote is a string
    assert len(res.json['quote']) > 0  # Ensure the quote is not empty  
def test_quote_endpoint():
    client = app.app.test_client()
    res = client.get('/quote')
    assert res.status_code == 200
    assert res.content_type == 'application/json'  # Ensure the response is JSON
    assert 'quote' in res.json  # Ensure the quote key is present in the response
    assert isinstance(res.json['quote'], str)  # Ensure the quote is a string
    assert len(res.json['quote']) > 0  # Ensure the quote is not empty
def test_quote_api_key():
    import os
    api_key = os.getenv("GROQ_API_KEY")
    assert api_key is not None, "GROQ_API_KEY environment variable is not set"
    assert isinstance(api_key, str) and len(api_key) > 0, "GROQ_API_KEY should be a non-empty string"
def test_quote_api_response():
    import os
    import requests

    api_key = os.getenv("GROQ_API_KEY")
    assert api_key is not None, "GROQ_API_KEY environment variable is not set"

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mixtral-8x7b-32768",
        "messages": [{"role": "user", "content": "Give me a short motivational quote."}]
    }

    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 200, "API request failed"
    result = response.json()
    assert 'choices' in result and len(result['choices']) > 0, "API response does not contain choices"
    assert 'message' in result['choices'][0], "API response does not contain message in choices"
    assert 'content' in result['choices'][0]['message'], "API response does not contain content in message"
    quote = result['choices'][0]['message']['content'].strip()
    assert isinstance(quote, str) and len(quote) > 0, "Quote should be a non-empty string"
    
