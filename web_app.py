from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask hidup di Railway ✅"

@app.route("/health")
def health():
    return "OK", 200
