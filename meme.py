from flask import Flask

app = Flask(__name__)

@app.route("/")
def meme_shop():
    return "Hey"

