import os
import sys
import requests

from logzero import logger
from configuration.config import Configuration


def get_subreddit_data(subreddit_name):
    config = Configuration()
    script_name = os.path.basename(__file__)
    script_config = config.get_config(script_name)
    try:
        response = requests.get("https://{0}/r/{1}.json".format(script_config["host"], subreddit_name))
        return response.text
    except Exception as e:
        logger.error(e)