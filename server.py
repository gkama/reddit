import sys

from flask import Flask
from scripts.subreddit import Subreddit


app = Flask(__name__)


@app.route("/subreddits")
def flask_get_subreddits():
    return get_subreddits()
