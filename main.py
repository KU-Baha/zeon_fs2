import sys
from init_fs import init_fs
from list_files import file_list
from add_file import add_file
from del_file import del_file

commands = {
    'init': init_fs,
    'list': file_list,
    'add': add_file,
    'del': del_file
}

argv = sys.argv

if len(argv) <= 1:
    print("Write command!")
    exit(0)

_, command, *args = argv

if command not in commands:
    print("Command not found!")
    exit(0)

commands[command](*args)
