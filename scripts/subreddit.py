import sys
import requests

from logzero import logger


def get_subreddit_data(subreddit_name):
    try:
        response = requests.get("https://www.reddit.com/r/{0}.json".format(subreddit_name))
        return response.text
    except Exception as e:
        logger.error(e)