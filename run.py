import sys

from config import Configuration
from scripts.subreddit import *
from logzero import logger


def main(argv):
    try:
        if argv[1:]:
            script_name = argv[1]
            if argv[2:]:
                script_input = argv[2:]
    except Exception as e:
        logger.error("couldn't find configuration for specified script")
        sys.exit()

    config = Configuration()
    script_config = config.get_config(script_name)
    
    print(get_subreddit_data("personalfinance"))


if __name__ == "__main__":
    main(sys.argv[0:])