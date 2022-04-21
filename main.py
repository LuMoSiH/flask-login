from flask import Flask, render_template, redirect, url_for, session, flash, request
from flask_session import Session
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd

app = Flask(__name__, static_folder="./static", template_folder="templates")
app.secret_key = "U2VjcmV0a2V5THVhbk1vcmVuZ3Vp"
# Config session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.permanent_session_lifetime = timedelta(days=7)
Session(app)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/SignUp")
def SignUp():
    return render_template("SignUp.html")


@app.route("/register", methods=["POST"])
def register():
    login = request.form.get("login")
    password = generate_password_hash(request.form.get("password"))
    # FORM VALIDATION
    if not login:
        flash("Missing login", "secondary")
        return redirect("/SignUp")

    if len(request.form.get("password")) == 0:
        flash("Missing password", "secondary")
        return redirect("/SignUp")

    users.loc[len(users)] = [login, password]

    #print(users.index(login))


    return redirect("/")


@app.route("/logon", methods=["POST"])
def logon():
    login = request.form.get("cpf")
    password = request.form.get("password")
    remember = request.form.get("remember")
    # Form Validation
    if not login:
        flash("Missing CPF", "secondary")
        return redirect("/login")

    if not password:
        flash("Missing password", "secondary")
        return redirect("/login")

    return redirect(url_for("/"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)