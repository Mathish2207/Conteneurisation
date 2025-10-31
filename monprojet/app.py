from flask import Flask, jsonify
from pathlib import Path

app = Flask(__name__)

def load_quotes():
    with Path("data/quotes.txt").open() as fh:
        return [line.strip() for line in fh if line.strip()]

QUOTES = load_quotes()

@app.route("/")
def home():
    return jsonify(QUOTES)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
