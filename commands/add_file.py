import os
import sys

from helper.helper import add_file


def main():
    argv = sys.argv

    if len(argv) <= 1:
        print("Write arguments!")
        exit(0)

    _, *args = argv

    add_file(os.getcwd(), *args)


if __name__ == '__main__':
    main()
