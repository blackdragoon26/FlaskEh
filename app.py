from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask on WSL 2!"

@app.route("/fuckit")
def ohyeah():
    return "yeah, die soon, man!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

