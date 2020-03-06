import os
import sys
import requests

from logzero import logger
from auth import Authentication


class Subreddit(object):
    def __init__(self):
        self._reddit_client = Authentication().GetRedditClient()


    def getSubreddit(self, subreddit_name):
        return self._reddit_client.subreddit(subreddit_name)


    def getHotTenSubreddit(self, subreddit_name):
        return self._reddit_client.subreddit(subreddit_name).hot(limit=10)

    
    def getTopTenSubreddit(self, subreddit_name):
        posts = self._reddit_client.subreddit(subreddit_name).top(limit=10)
        for post in posts:
            print(post)