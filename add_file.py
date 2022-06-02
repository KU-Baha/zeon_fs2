import sys
import shutil
from pathlib import Path

BASE_DIR_PATH = "zeon_fs2"

argv = sys.argv

if len(argv) != 2:
    print("Write 1 argument!")
    exit(0)

file_path = argv[1]

if not Path(file_path).exists():
    print("File does not exists!")
    exit(0)

file_name = Path(file_path).name_f

if Path(f"{BASE_DIR_PATH}/{file_name}").exists():
    print(f"File already exists in {BASE_DIR_PATH}")
    exit(0)

shutil.copy(file_path, f"{BASE_DIR_PATH}/{file_name}")
print("Success")
