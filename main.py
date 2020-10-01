from flask import Flask, g, render_template, request
from database import init_db

app = Flask("app", static_folder="public", template_folder="views")

with app.app_context():
    init_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/stock-prices", methods=["GET"])
def check_stocks():
    pass


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
