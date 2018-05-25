from flask import Flask
from flask import jsonify
import websites.hsTopDecks

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to my API!"

@app.route("/hsTopDecks")
def getHsTopDecks():
    deckLists = websites.hsTopDecks.getDeckLists()
    return jsonify(deckLists)


if __name__ == '__main__':
    app.run(debug=True)