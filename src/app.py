from flask import Flask, render_template
import os


app = Flask(
    __name__,
    template_folder="templates",
    static_folder="css",
    static_url_path="/src/assets",
)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()

