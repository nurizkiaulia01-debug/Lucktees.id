from flask import Flask, render_template, request, jsonify
from core import get_bot_reply

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    reply = get_bot_reply(user_msg)
    return jsonify({"reply": reply})

# penting untuk local test (Railway aman)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
