import os
import requests
import random
import time
from dotenv import load_dotenv
from pathlib import Path

# Load .env
load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

def get_quote():
    api_key = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"

    if not api_key:
        return "⚠️ API key missing."

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    fantasy_prompts = [
        "Craft a short fantasy quote (1–3 poetic lines) that ends with a fictional character name and their epic title.",
        "Generate a wise quote that a god would whisper before a celestial war. Keep it under 2 lines and end with a fictional name and role.",
        "Write a fallen king’s final reflection in 3 lines or less. Include their name and noble title at the end.",
        "Create a battle cry or farewell line from a rogue entering a deadly dungeon. Limit it to 1 line. End with their alias and class.",
        "Imagine what an ancient dragon would carve into the stone walls of its lair. Keep it 1–3 lines, with author name and legendary title.",
        "Whisper a teaching from a powerful mage to their apprentice in under 2 lines. End with their full mystical title.",
        "Generate a quote etched into a crumbling pixel-art gravestone. Short, epic, and signed by a character with class and title.",
        "Write the last words of a time-traveling paladin. Limit it to 3 lines and end with a fantasy signature.",
        "Give a cryptic message a sword might whisper to its bearer. Make it under 2-3 lines and signed by the sword’s name or its past wielder.",
        "Compose a quote found on an ancient dungeon gate, cursed scroll, or glowing obelisk. Must be 1–3 lines and include name + fantasy role.",
        "What would a deity of forgotten realms say in 3 lines before fading into myth? Include their divine name and realm.",
        "Write a final lesson passed down in a glowing 8-bit temple. No more than 3 lines. Conclude with a fictional character and class.",
        "What is written in the Book of Eternal Trials, right before the hero ascends? 1 line max, and end with a named sage or monk.",
        "What would a rune-inscribed statue speak in 3 cryptic lines? Sign off with a name like a Dungeon Architect or Guardian.",
        "Give a message from a vanished realm’s last oracle. Short, haunting, and ends with the oracle’s name and domain."
    ]

    prompt = random.choice(fantasy_prompts)

    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "system",
                "content": "You are a wise fantasy quote generator. Format all responses as short quotes (1–3 lines), ending with a fictional name and title. Do not include images, ASCII art, emoji, or visual elements."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, json=data, timeout=10)
            if response.status_code != 200:
                continue

            result = response.json()
            quote = result.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
            return quote if quote else "⚠️ The sages returned no wisdom."

        except requests.exceptions.RequestException as e:
            time.sleep(1)  # Small delay before retry

    return "⚠️ The realm is silent. No quote could be retrieved after multiple attempts."
