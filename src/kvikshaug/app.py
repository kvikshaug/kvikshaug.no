from flask import Flask, render_template
from jinja2 import StrictUndefined

from .settings import Configuration


app = Flask(
    "kvikshaug", template_folder="../../templates", static_folder="../../assets"
)
app.config.from_object(Configuration)
if app.config["DEBUG"]:
    # Be strict during development; forgiving in production.
    app.jinja_env.undefined = StrictUndefined


@app.route("/")
def home():
    return render_template("layout.html")
