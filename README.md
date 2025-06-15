# ⚔️ AI Dungeon Quote Generator

A pixel-styled fantasy quote generator powered by Groq’s LLM API. Generates short, poetic quotes attributed to fictional RPG characters (like gods, dragons, and dungeon kings) with a stylized frontend and a secure backend.

---

## 🌐 Live Demo

> Local: `http://localhost:5000`

---

## 🚀 Features

- 🎲 Random fantasy-style prompts with 1–3 line responses
- 🧙 Character-signed quotes (e.g., `— Kael the Timeless, Mage of Ashes`)
- 🎮 Retro dungeon UI with bounce animations & toggleable light/dark mode
- 🔁 Looping background music during quote generation
- ⚔️ Secure API route with restricted access to frontend only
- 💬 LLM-powered backend with error handling, retry logic, and timeout safety

---

## 🧱 Tech Stack

| Layer | Tech |
|-------|------|
| Frontend | HTML, CSS (custom), JavaScript |
| Backend | Python, Flask |
| AI | Groq API (`llama3-8b-8192` model) |
| DevOps | Git, GitHub, `.env` management |
| (Optional) | Terraform for IaC, Dockerfile for containerization |

---

## 🛠️ How to Run

```bash
git clone https://github.com/yourusername/ai-quote-generator
cd ai-quote-generator
python -m venv venv
source venv/bin/activate  # or `venv\\Scripts\\activate` on Windows
pip install -r requirements.txt
touch .env
