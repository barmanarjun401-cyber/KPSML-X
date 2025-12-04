from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Abanime Flask server is running!"
