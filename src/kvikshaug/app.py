from datetime import datetime
import json
import os

from flask import Flask, render_template, request, redirect
from jinja2 import StrictUndefined

from .settings import Configuration


app = Flask(
    "kvikshaug", template_folder="../../templates", static_folder="../../assets"
)
app.config.from_object(Configuration)
if app.config["DEBUG"]:
    # Be strict during development; forgiving in production.
    app.jinja_env.undefined = StrictUndefined

# Initialize guestbook if not yet created.
if not os.path.exists("data/guestbook.json"):
    with open("data/guestbook.json", "w") as file_:
        json.dump([], file_)


@app.route("/")
def home():
    with open("data/guestbook.json") as file_:
        guestbook = [c for c in json.load(file_) if c["published"]]
    for message in guestbook:
        message["datetime"] = datetime.strptime(message["datetime"], "%Y-%m-%d %H:%M")
    guestbook = sorted(guestbook, key=lambda m: m["datetime"], reverse=True)
    return render_template("layout.html", guestbook=guestbook)


@app.route("/guestbook", methods=["POST"])
def guestbook():
    message = request.form.get("message", "").strip()
    if message == "":
        return redirect("/#guestbook")
    with open("data/guestbook.json") as file_:
        guestbook = json.load(file_)
    with open("data/guestbook.json", "w") as file_:
        guestbook.append(
            {
                "message": message,
                "ip": request.remote_addr,
                "datetime": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "published": False,
            }
        )
        json.dump(guestbook, file_)
    return redirect("/#guestbook")
