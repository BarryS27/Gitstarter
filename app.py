from flask import Flask, render_template, request
from helpers import search_issues

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        lang = request.form.get("language")
        if not lang:
            return "Please enter the language you want."
        issues = search_issues(lang)
        return render_template("index.html", results=issues, search_term=lang)
    else:
        return render_template("index.html", results=[])
