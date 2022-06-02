import sys
import shutil
from pathlib import Path
from config import BASE_DIR


def add_file(*args) -> bool:
    if len(args) != 1:
        print("Write 1 argument!")
        return False

    file_path = args[0]

    if not Path(file_path).exists():
        print("File does not exists!")
        exit(0)

    file_name = Path(file_path).name

    if Path(f"{BASE_DIR}/{file_name}").exists():
        print(f"File already exists in {BASE_DIR}")
        exit(0)

    shutil.copy(file_path, f"{BASE_DIR}/{file_name}")
    print("Success")

    return True
