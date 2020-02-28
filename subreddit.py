import os
import sys
import requests

from logzero import logger
from config import Configuration


class Subreddit(object):
    def __init__(self):
        self._config = Configuration()
        self._script_name = os.path.basename(__file__)
        self._script_config = self._config.get_config(self._script_name)


    def get_subreddits(self):
        try:
            subreddits = list()
            for sub in self._script_config["subreddits"]:
                subreddits.append(sub["name"])
            return subreddits
        except Exception as e:
            logger.error(e)