from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "smart-internship-secret-key"

users = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return "Passwords do not match"

        if email in users:
            return "Email already registered"

        users[email] = {
            "name": name,
            "password": generate_password_hash(password)
        }

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        if email not in users:
            return "User not found"

        if not check_password_hash(users[email]["password"], password):
            return "Incorrect password"

        session["email"] = email

        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "email" not in session:
        return redirect(url_for("login"))

    email = session["email"]
    name = users[email]["name"]

    return render_template("dashboard.html", name=name)


@app.route("/logout")
def logout():

    session.pop("email", None)

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)