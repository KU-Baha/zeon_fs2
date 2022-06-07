import shutil
import sys
from os import path
from pathlib import Path

args = sys.argv

if len(args) != 2:
    print("wrong arguments")
    exit(0)

source_file = args[1]
if not path.isfile(source_file):
    print("it's not a file")
    exit(0)

file_name = Path(source_file).name

if path.isfile("zeon_fs2/" + file_name):
    print("we already have this file")
    exit(0)

shutil.copyfile(source_file, "zeon_fs2/" + file_name)