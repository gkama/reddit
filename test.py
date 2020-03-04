import sys

from config import Configuration
from auth import Authentication


def main(argv):
    config = Configuration()
    auth = Authentication()
    #print(config.get_config(".\\subreddit.py"))
    auth.get()


if __name__ == "__main__":
    main(sys.argv[0:])