from flask import Flask, jsonify, send_from_directory
from quotes import get_quote
import os

app = Flask(__name__, static_folder="../templates")

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/q1x99y")
def serve_quote():
    return jsonify({"quote": get_quote()})

# ✅ THIS IS WHAT VERCEL NEEDS:
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
