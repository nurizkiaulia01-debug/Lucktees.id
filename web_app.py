import os
from flask import Flask, render_template, request, jsonify
from core import get_bot_reply

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_message = data.get("message", "")
    reply = get_bot_reply(user_message)
    return jsonify({"reply": reply})

# ❌ JANGAN pakai app.run() di Railway
# Gunicorn yang akan menjalankan app
