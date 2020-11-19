from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def register_view():
    return render_template("login/login.html")

@app.route("/register")
def login_view():
    return render_template("register.html")


if __name__=="__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
