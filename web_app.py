import os
from flask import Flask, render_template, request, jsonify
from core import get_bot_reply

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates")
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "")
    reply = get_bot_reply(user_message)
    return jsonify({"reply": reply})
