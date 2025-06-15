import os
import random
from groq import Groq, APIConnectionError, RateLimitError

# No need for dotenv here, Vercel handles environment variables

def get_quote():
    api_key = os.environ.get("GROQ_API_KEY")

    if not api_key:
        return "⚠️ Critical error: API key is not configured on the server."

    try:
        client = Groq(
            api_key=api_key,
            max_retries=4,
            timeout=15.0,
        )
    except Exception:
        return "⚠️ API client could not be initialized."

    fantasy_prompts = [
        "Craft a short fantasy quote (1–3 poetic lines) that ends with a fictional character name and their epic title.",
        "Generate a wise quote that a god would whisper before a celestial war. Keep it under 2 lines and end with a fictional name and role.",
        "Write a fallen king’s final reflection in 3 lines or less. Include their name and noble title at the end.",
        "Create a battle cry or farewell line from a rogue entering a deadly dungeon. Limit it to 1 line. End with their alias and class.",
        "Imagine what an ancient dragon would carve into the stone walls of its lair. Keep it 1–3 lines, with author name and legendary title.",
    ]
    prompt = random.choice(fantasy_prompts)

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a wise fantasy quote generator. Format all responses as short quotes (1–3 lines), ending with a fictional name and title. Do not include images, ASCII art, emoji, or visual elements."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama3-8b-8192",
        )
        quote = chat_completion.choices[0].message.content.strip()
        return quote if quote else "⚠️ The sages returned no wisdom."
    except RateLimitError:
        return "⚠️ The realm is overwhelmed by requests. Please try again in a moment."
    except APIConnectionError:
        return "⚠️ The realm is silent. Could not connect to the sages."
    except Exception:
        return "⚠️ A mysterious force prevented wisdom from being retrieved."