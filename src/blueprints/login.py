from flask import (
    Blueprint,
    render_template,
)


login = Blueprint(
    "login",
    __name__,
)


@login.route("/login", methods=["GET", "POST"])
def user_login():
    return render_template("login.html")
