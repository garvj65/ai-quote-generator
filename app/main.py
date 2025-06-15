from flask import Flask, jsonify
from app.quotes import get_quote

app = Flask(__name__)

@app.route("/quote")
def quote():
    return jsonify({"quote": get_quote()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# This is the main entry point for the Flask application.
# It defines a single route that returns a random quote in JSON format.