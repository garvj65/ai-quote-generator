# 🤖 AI Quote Generator (Groq-Powered)

This Flask API returns a motivational quote using Groq's blazing-fast inference API (Mixtral).

## 🧠 Features
- `/quote` endpoint (GET)
- Groq integration using Mixtral-8x7B
- Dockerized + GitHub Actions CI/CD
- Terraform for cloud infra (mock)

## 🚀 Setup

```bash
# Setup virtualenv
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Run the app
export GROQ_API_KEY=your_key
python app/main.py
