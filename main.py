import os
import argparse
import constant
import webcrawler


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main():
    clear()


if __name__ == "__main__":
    main()
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--threads", help=constant.ARG_HTTP_THREADING_HELP, type=int, dest="threads", default=10)
    parser.add_argument("-u", "--target", help=constant.ARG_TARGET_HELP, type=str, dest="target", required=True)
    parser.add_argument("-o", "--output", help=constant.ARG_OUTPUT_HELP, type=str, dest="output")
    args = parser.parse_args()
