from flask import Flask, jsonify, request, render_template
from quotes import get_quote

app = Flask(__name__, static_folder="static", template_folder="../templates")

@app.route("/")
def serve_frontend():
    return render_template("index.html")

@app.route("/q1x99y")
def serve_quote():
    return jsonify({"quote": get_quote()})

def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
