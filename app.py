from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style=text-align:center> Hi! I am Giorgi Tamarashvili, nice to meet you :)<h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
