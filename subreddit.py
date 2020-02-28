import os
import sys
import requests

from logzero import logger
from config import Configuration


class Subreddit(object):
    def __init__(self):
        self.config = Configuration()
        self.script_name = os.path.basename(__file__)
        self.script_config = config.get_config(script_name)


    def get_subreddits(self):
        try:
            subreddits = list()
            for sub in self.script_config["subreddits"]:
                subreddits.append(sub["name"])
            return subreddits
        except Exception as e:
            logger.error(e)