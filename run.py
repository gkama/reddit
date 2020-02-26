from scripts.subreddit import *

def main(argv):
    script_name = argv[1]
    print("in in run.py")
    print("script name " + script_name)
    print(get_str())


if __name__ == "__main__":
    main(sys.argv[0:])