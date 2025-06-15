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

def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
