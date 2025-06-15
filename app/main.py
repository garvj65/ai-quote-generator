from flask import Flask, jsonify, render_template
from quotes import get_quote

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quote")
def quote():
    return jsonify({"quote": get_quote()})
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404 
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)