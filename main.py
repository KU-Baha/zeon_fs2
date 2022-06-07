import os
import sys
from command import commands_list


def main():
    argv = sys.argv

    if len(argv) <= 1:
        print("Write command!")
        exit(0)

    _, command, *args = argv

    if command not in commands_list:
        print("Command not found!")
        exit(0)

    dir_path = os.getcwd()

    commands_list[command](dir_path, *args)


if __name__ == '__main__':
    main()
