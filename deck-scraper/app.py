from flask import Flask
import websites.hsTopDecks

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hsTopDecks")
def getHsTopDecks():
    return websites.hsTopDecks.getDeckLists()

if __name__ == '__main__':
    app.run(debug=True)