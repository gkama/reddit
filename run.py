from scripts.subreddit import *
from logzero import logger


def main(argv):
    script_name = argv[1]
    logger.info("test")
    print("in in run.py")
    print("script name " + script_name)
    print(get_str())


if __name__ == "__main__":
    main(sys.argv[0:])