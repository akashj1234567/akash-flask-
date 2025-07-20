from flask import Flask

app = Flask(__name__)


@app.route("/wish")
def wish():
    return "<h1>Good morning Docker don!<h1>"

@app.route("/login")
def login():
    return "<h1>here is login page!<h1>"


if __name__=="__main__":
    app.run(port=5000 , host= "0.0.0.0")
        