from flask import Flask, render_template, request
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///kombinacie.db")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        magistro = request.form.get("magistro")
        common = request.form.get("common")
        # Get database
        priznaky = db.execute(
            "SELECT "
            + magistro
            + " FROM kombinaciePriznakov WHERE Surovina = '"
            + common
            + "';"
        )
        priznaky = priznaky[0][magistro]

        return render_template(
            "cooking.html", magistro=magistro, common=common, priznaky=priznaky
        )
