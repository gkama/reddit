import sys

from flask import Flask
from subreddit import Subreddit


app = Flask(__name__)
sub = Subreddit()

@app.route("/subreddits")
def flask_get_subreddits():
    return sub.get_subreddits()
