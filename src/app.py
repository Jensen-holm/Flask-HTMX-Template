from flask import Flask, render_template
import os


app = Flask(
    __name__,
    template_folder="templates",
    static_folder="css",
    static_url_path="/src/assets",
)


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template(
        "login.html",
    )


@app.route("/")
def index():
    return render_template(
        "index.html",
        name="Emily",
    )


if __name__ == "__main__":
    app.run()
