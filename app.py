from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "MindThreadRG is running successfully on Railway!"
