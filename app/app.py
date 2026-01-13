from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "Self-Healing App is Running 🚀"


@app.route("/crash")
def crash():
    os._exit(1)   # force container crash


if __name__ == "__main__":
    app.run("0.0.0.0",port=5000)
