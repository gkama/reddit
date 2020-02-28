import sys

from flask import Flask
from scripts.subreddit import *


app = Flask(__name__)


@app.route("subreddit/<name>")
def get_subreddit_data(name):
    return get_subreddit_data(name)
