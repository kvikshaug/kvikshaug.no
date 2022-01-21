from flask import Flask, render_template
from jinja2 import StrictUndefined

from .settings import Configuration


app = Flask("kvikshaug", template_folder="../../templates")
app.config.from_object(Configuration)
if app.config["DEBUG"]:
    # Be strict during development; forgiving in production.
    app.jinja_env.undefined = StrictUndefined


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")
