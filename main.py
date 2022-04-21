from flask import Flask, render_template, redirect, url_for, session, flash, request
from flask_session import Session
from datetime import timedelta
import sqlite3
import random

# Config App
app = Flask(__name__, static_folder="./static", template_folder="templates")
app.secret_key = "U2VjcmV0a2V5THVhbk1vcmVuZ3Vp"#<<<<< INSERT YOUR SECRET KEY
# Config session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# Time Session
app.permanent_session_lifetime = timedelta(days=7)
Session(app)


def get_db_connection():
    conn = sqlite3.connect("db.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    # Session validation
    if not session.get("login"):
        return redirect("/login")
    # Random image welcome
    welcome = [
        'https://media2.giphy.com/media/dZXzmKGKNiJtDxuwGg/giphy.gif?cid=ecf05e475nnedi7zay7w7brr9rmj112tyqdsqfoyy276jejm&rid=giphy.gif&ct=g',
        'https://media2.giphy.com/media/EKrFksrzxQxlb5ahiq/giphy.gif?cid=ecf05e475nnedi7zay7w7brr9rmj112tyqdsqfoyy276jejm&rid=giphy.gif&ct=g',
        'https://media4.giphy.com/media/l4JyOCNEfXvVYEqB2/giphy.gif?cid=ecf05e475nnedi7zay7w7brr9rmj112tyqdsqfoyy276jejm&rid=giphy.gif&ct=g'
    ]

    return render_template("index.html", img=random.choice(welcome))


@app.route("/login")
def login():
    # Session validation
    if session.get("login"):
        return redirect("/")
    return render_template("login.html")


@app.route("/logon", methods=["POST"])
def logon():
    login = request.form.get("login")
    password = request.form.get("password")
    remember = request.form.get("remember")
    # Form Validation
    if not login:
        flash("Missing login", "secondary")
        return redirect("/login")

    if not password:
        flash("Missing password", "secondary")
        return redirect("/login")

    # Verify if account exist
    conn = get_db_connection()
    account = conn.execute(f"SELECT * FROM users where login='{login}'").fetchone()
    conn.close()

    if account and password == account['password']:
        # Session On or Off - 7 Days
        match remember:
            case "None":
                session.permanent = False
            case "on":
                session.permanent = True

        session["login"] = account['login']  # login

        return redirect("/")

    flash("Invalid credentials", "secondary")
    return redirect("/login")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)