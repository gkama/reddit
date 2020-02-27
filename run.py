import sys

from config import Configuration
from scripts.subreddit import *
from logzero import logger


def main(argv):
    try:
        if argv[1:]:
            script_name = argv[1]
            if argv[2:]:
                script_inputs = argv[2:]
    except Exception as e:
        logger.error("couldn't find configuration for specified script")
        sys.exit()

    logger.info("getting configuration for script={0}".format(script_name))
    config = Configuration()
    script_config = config.get_config(script_name)
    json_config = config.get_json_config()

    if script_name == "subreddit":
        subr = script_inputs[0]
        logger.info("running script={0} with input={1}".format(script_name, script_inputs[0]))


if __name__ == "__main__":
    main(sys.argv[0:])