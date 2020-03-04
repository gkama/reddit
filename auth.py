import sys
import os
import requests
import praw

from config import Configuration
from logzero import logger


class Authentication(object):
    def __init__(self):
        self.config = Configuration()
        self.config_json = self.config.get_json_config()
        self.reddit = praw.Reddit(client_id=self.config_json["clientId"],
                     client_secret=self.config_json["clientSecret"],
                     user_agent="myuniqueid")


    def getToken(self):
        logger.info("getting Reddit API token")


    def get(self):
        for submission in self.reddit.subreddit('learnpython').hot(limit=10):
            print(submission.title)