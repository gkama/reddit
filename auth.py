import sys
import os
import requests
import praw
import uuid

from config import Configuration
from logzero import logger


class Authentication(object):
    def __init__(self):
        self._config = Configuration()
        self._config_json = self._config.get_json_config()
        self._reddit = praw.Reddit(client_id=self._config_json["clientId"],
                     client_secret=self._config_json["clientSecret"],
                     user_agent=str(uuid.uuid4()))


    def GetRedditClient(self):
        logger.info("getting Reddit API (Praw) client")
        return self._reddit