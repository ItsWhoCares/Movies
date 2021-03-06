import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route("/")
# @login_required
def index():
    """Show portfolio of stocks"""
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    q = request.args.get("q")
    print(q)
    result = lookup(q)
    print(result['results'][0]['image'])
    return render_template("img.html", url=result['results'][0]['image'])