from functools import wraps

from flask import Flask, flash, redirect, render_template, request, session, url_for

from config import Config


app = Flask(__name__)
app.config.from_object(Config)


def admin_required(view):
    @wraps(view)
    def protected_view(*args, **kwargs):
        if not session.get("admin_authenticated"):
            return redirect(url_for("admin_login"))
        return view(*args, **kwargs)

    return protected_view


@app.get("/")
def home():
    return render_template("index.html", profile={"name": "Aarav Mehta"})


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        if email == app.config["ADMIN_EMAIL"] and password == app.config["ADMIN_PASSWORD"]:
            session["admin_authenticated"] = True
            return redirect(url_for("admin_dashboard"))
        flash("Invalid admin credentials.", "error")
    return render_template("admin_login.html")


@app.get("/admin")
@admin_required
def admin_dashboard():
    return render_template("admin_dashboard.html", firebase_config=app.config["FIREBASE_CONFIG"])


@app.get("/admin/logout")
def admin_logout():
    session.clear()
    return redirect(url_for("admin_login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(__import__("os").environ.get("PORT", "5000")))
