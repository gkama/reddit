import sys

from config import Configuration
from auth import Authentication
from subreddit import Subreddit


def main(argv):
    sub = Subreddit()
    sub.getHotTenSubreddit("personalfinance")


if __name__ == "__main__":
    main(sys.argv[0:])