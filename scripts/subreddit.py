import os
import sys
import requests

from logzero import logger
from config import Configuration


config = Configuration()
script_name = sys.argv[0]
script_config = config.get_config(script_name)


def get_subreddit_data(subreddit_name):
    try:
        response = requests.get("https://{0}/r/{1}.json".format(script_config["host"], subreddit_name))
        return response.text
    except Exception as e:
        logger.error(e)