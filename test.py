import sys

from config import Configuration


def main(argv):
    config = Configuration()
    print(config.get_config(".\\subreddit.py"))


if __name__ == "__main__":
    main(sys.argv[0:])